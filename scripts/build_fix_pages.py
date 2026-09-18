#!/usr/bin/env python3
"""Render /fix/<tool>/index.html pages from one template + per-tool data.

Grug-simple: no templating library, just str.format with a shared HTML
skeleton. Run from repo root: python3 scripts/build_fix_pages.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TOOLS = {
    "cursor": {
        "name": "Cursor",
        "tagline": "Cursor App Broken? I Fix It.",
        "meta_desc": "Cursor generated code that crashes, corrupts files, or breaks on every edit? A senior engineer (10+ yrs) fixes Cursor-built apps fast. Flat fees from $2,500.",
        "intro": (
            "You built it fast in Cursor. Now every change breaks two other things, "
            "files silently fail to save, or the agent edited code you never asked it to touch. "
            "Cursor is a great prototyping tool and a rough production tool &mdash; here's why, "
            "and how I fix it."
        ),
        "failures": [
            (
                "Context loss on larger repos",
                "Cursor builds its understanding from open files and its index. Once a "
                "project spans more than a handful of files, it can't see everything at "
                "once &mdash; so it guesses, edits files unrelated to your request, or "
                "invents functions that don't exist in your codebase.",
            ),
            (
                "Cascading fixes",
                "Ask Cursor to fix one bug and it patches the symptom, not the cause. The "
                "fix breaks two other things, which need their own fixes, which break two "
                "more. Tangled logic in a single large file makes this worse.",
            ),
            (
                "Silent save failures",
                "Cursor has shipped updates where files failed to save reliably, or chat "
                "history and worktrees got corrupted. What you see in the editor isn't "
                "always what's actually on disk.",
            ),
            (
                "Unreviewed autonomous edits",
                "Agent mode changes files you didn't ask it to touch &mdash; auth logic, "
                "config, unrelated components &mdash; and reports success even when it "
                "changed the wrong thing. Repo-triggered exploit classes (like prompt "
                "injection via a malicious file) have also been documented against "
                "agentic IDEs, including Cursor.",
            ),
            (
                "Diffing and merge instability",
                "Version updates have broken Cursor's diff view outright, making review "
                "impossible and leading teams to merge changes blind &mdash; which is how "
                "small bugs turn into production incidents.",
            ),
        ],
        "faq": [
            (
                "Do I need to switch off Cursor to work with you?",
                "No. I meet your code where it is. If Cursor is still useful for your team "
                "day to day, keep using it &mdash; I fix what's broken and set up guardrails "
                "so the next AI-generated change doesn't reintroduce the same bugs.",
            ),
            (
                "My Cursor-built app worked yesterday and doesn't today. What happened?",
                "Usually an agent edit touched something outside the scope you asked for, "
                "or an update changed how Cursor applies diffs. I diagnose the actual git "
                "history to find the exact change, not just the symptom.",
            ),
            (
                "Can you tell if Cursor introduced a security issue?",
                "Yes &mdash; auth logic, exposed keys, and unreviewed autonomous edits are "
                "exactly what I audit for first. If something's exposed, you'll know within "
                "the diagnostic.",
            ),
            (
                "Is my app too far gone to fix?",
                "Rarely. Most Cursor rescues are a Stabilize engagement, not a rebuild. "
                "I'll tell you honestly if a targeted rebuild is actually faster.",
            ),
        ],
    },
    "lovable": {
        "name": "Lovable",
        "tagline": "Lovable App Broken? I Fix It.",
        "meta_desc": "Lovable app works in preview but breaks in production? A senior engineer (10+ yrs) fixes Lovable-built apps fast. Flat fees from $2,500. Free diagnostic.",
        "intro": (
            "Your Lovable app looked perfect in preview. Then you deployed it, a second "
            "user showed up, and it fell over. That gap between preview and production is "
            "the single most common thing I fix in Lovable apps &mdash; here's why it "
            "happens."
        ),
        "failures": [
            (
                "Environment variables vanish at deploy",
                "Lovable's preview environment has your env vars set for you. Your actual "
                "host (Vercel, Netlify, wherever) doesn't &mdash; until you add them "
                "manually. This alone causes most \"it worked yesterday\" deploy failures: "
                "blank screens, 500s, silent auth failures.",
            ),
            (
                "Supabase RLS misconfigured",
                "Lovable wires up Supabase fast, but row-level security policies are often "
                "an afterthought: either locked down so tight your own app can't query its "
                "data, or missing entirely so any user can read anyone else's rows.",
            ),
            (
                "Auth that works solo, breaks with real users",
                "It works when you click around alone. It breaks the moment two people are "
                "logged in at once &mdash; session handling and auth redirects behave "
                "differently on the live domain than they did in preview.",
            ),
            (
                "Stripe and webhooks untested in live mode",
                "Checkout flows built and tested in Stripe test mode fail against real "
                "webhook signatures, or checkout succeeds while the app's access state "
                "never updates.",
            ),
            (
                "Architecture that collapses past ~10 concurrent sessions",
                "Lovable optimizes for speed of generation, not load. Database connections "
                "and query patterns that are fine for a demo start timing out or dropping "
                "under real concurrent traffic.",
            ),
        ],
        "faq": [
            (
                "My app works when I test it but not for real users. Why?",
                "Almost always a preview-vs-production gap: missing env vars, RLS rules "
                "that don't match production auth, or connection handling that wasn't "
                "built for concurrent sessions. I check all three first.",
            ),
            (
                "Do you work with Supabase?",
                "Yes &mdash; Supabase is the default backend for most Lovable apps, so RLS "
                "audits and auth fixes are routine work here.",
            ),
            (
                "Can you fix a broken Stripe integration?",
                "Yes. Test-mode-to-live-mode gaps in checkout and webhook handling are one "
                "of the most common Lovable production bugs I see.",
            ),
            (
                "How fast can you diagnose a deploy failure?",
                "Free diagnostic within 48 hours. Most Lovable deploy failures trace back "
                "to one of five known causes, so I usually know within the first look.",
            ),
        ],
    },
    "bolt": {
        "name": "Bolt.new",
        "tagline": "Bolt.new App Broken? I Fix It.",
        "meta_desc": "Bolt.new app burning tokens, failing to deploy, or 500ing in production? A senior engineer (10+ yrs) fixes Bolt-built apps fast. Flat fees from $2,500.",
        "intro": (
            "Bolt gets you about 70% of the way to a working app fast. The last 30% "
            "&mdash; the part that actually survives production traffic &mdash; is where "
            "most Bolt apps I see are stuck. Here's what typically breaks."
        ),
        "failures": [
            (
                "Runaway token usage from fix loops",
                "You ask Bolt to fix a bug, the fix creates a new bug, Bolt tries to fix "
                "that, and so on. Each attempt consumes tokens, and because Bolt includes "
                "the whole codebase in every request, costs climb fast until you hit a hard "
                "prompt-length limit and the project stalls.",
            ),
            (
                "Build succeeds, runtime fails",
                "The app builds fine and then 500s on the first real request. Usual "
                "culprits: server-only code written against Bolt's preview runtime, "
                "hardcoded preview URLs, or a database connection configured for Bolt's "
                "environment instead of your production one.",
            ),
            (
                "TypeScript errors the dev server ignores",
                "Bolt's live preview tolerates type errors that a real production build "
                "step won't. The app looks done until you actually try to build it for "
                "deploy.",
            ),
            (
                "Case-sensitive import paths",
                "Imports that resolve fine in Bolt's environment break on Linux-based build "
                "servers where the filesystem is case-sensitive &mdash; a deploy failure "
                "that has nothing to do with your logic.",
            ),
            (
                "Missing environment variables at deploy",
                "Same pattern as most AI builders: the preview has secrets configured, "
                "your actual host doesn't, and nobody notices until the deployed app can't "
                "reach its own database.",
            ),
        ],
        "faq": [
            (
                "My Bolt project hit a token limit and won't respond anymore. Can you save it?",
                "Yes. I work directly with the exported code, not inside Bolt's chat loop, "
                "so a stalled project isn't a dead end &mdash; I fix the underlying bug "
                "instead of asking the AI to try again.",
            ),
            (
                "Why does my app work in Bolt's preview but not once deployed?",
                "Preview and production are different environments. Env vars, import "
                "case-sensitivity, and TypeScript strictness all differ &mdash; I check all "
                "three in the diagnostic.",
            ),
            (
                "Is a full rebuild ever necessary for a Bolt app?",
                "Sometimes, if fix-loop damage has left the codebase genuinely tangled. "
                "I'll tell you honestly whether Stabilize or Rebuild Right is the faster "
                "path.",
            ),
            (
                "Do you need Bolt access to fix this?",
                "No. Read-only access to your exported repo is enough. I don't need to "
                "work inside Bolt itself.",
            ),
        ],
    },
    "replit": {
        "name": "Replit",
        "tagline": "Replit App Broken? I Fix It.",
        "meta_desc": "Replit Agent broke a feature, looped without fixing the bug, or touched your production database? A senior engineer (10+ yrs) fixes Replit apps. Flat fees from $2,500.",
        "intro": (
            "Replit Agent is fast and it's autonomous &mdash; which means when it makes a "
            "mistake, it can make a big one, touching files or data you never asked it to "
            "touch. Here's what I see most often in Replit-built apps that need rescuing."
        ),
        "failures": [
            (
                "Agent edits unrelated files",
                "You ask for one feature and something else stops working, because Agent "
                "modified a shared utility, config file, or base component while "
                "implementing the change &mdash; without telling you.",
            ),
            (
                "Fix loops that don't converge",
                "Agent keeps acting but the work doesn't progress: it rewrites the same "
                "component, undoes its own previous fix, flips package versions back and "
                "forth, and claims success while the original bug is still there.",
            ),
            (
                "No real auth model",
                "Agent adds login screens and session handling when asked, but without "
                "designing access control first. The result protects some routes and "
                "misses others entirely.",
            ),
            (
                "Destructive database actions",
                "This is documented, not hypothetical: Replit's agent has run destructive "
                "commands against a live production database, misreading empty query "
                "results as a bug to \"fix\" by deleting data. If your app touches real "
                "user data, this is the first thing I check.",
            ),
            (
                "Replit-specific config that breaks off-platform",
                "Hardcoded values or Replit-only environment behavior that works inside "
                "Replit's workspace and fails the moment the app deploys anywhere else.",
            ),
        ],
        "faq": [
            (
                "Can you tell what Agent actually changed?",
                "Yes. I diagnose against your git history to find exactly what Agent "
                "touched, including changes outside the scope you asked for.",
            ),
            (
                "I'm worried Agent already damaged production data. What now?",
                "Tell me in the application &mdash; mark it urgent. I check for destructive "
                "data operations first, before anything else, when Replit is the stack.",
            ),
            (
                "Do you fix the missing auth model or just patch symptoms?",
                "I fix the model. Patching individual routes after the fact just leaves "
                "the next gap for someone to find.",
            ),
            (
                "Can you migrate off Replit if that's the real fix?",
                "Yes, though it's not always necessary. Sometimes stabilizing in place is "
                "faster and cheaper &mdash; the diagnostic tells you which.",
            ),
        ],
    },
    "v0": {
        "name": "v0",
        "tagline": "v0 App Broken? I Fix It.",
        "meta_desc": "v0-generated UI looks great but the app underneath doesn't work? A senior engineer (10+ yrs) wires up and fixes v0-built frontends. Flat fees from $2,500.",
        "intro": (
            "v0 is genuinely good at one thing: generating polished-looking React "
            "components fast. It doesn't generate a working app. The gap between "
            "\"looks done\" and \"is done\" is where most v0 projects I see need help."
        ),
        "failures": [
            (
                "No backend logic",
                "v0 generates UI, not your API routes, database queries, or business "
                "logic. Someone still has to wire the polished frontend up to real data "
                "&mdash; and that wiring is where most of the actual bugs live.",
            ),
            (
                "Unrequested changes to working code",
                "Ask for a small tweak and v0 rewrites unrelated components or files, "
                "breaking things that worked a moment ago. Small requests turn into wide "
                "blast radius.",
            ),
            (
                "Security hidden behind polish",
                "Because generated components look finished, they ship without a security "
                "review. Missing input validation, exposed data, and other gaps common to "
                "AI-generated code go unnoticed because the UI looks production-ready.",
            ),
            (
                "Accessibility gaps",
                "Visually correct markup that misses semantic HTML and ARIA fundamentals "
                "&mdash; fine for a demo, a liability once real users (and audits) show "
                "up.",
            ),
            (
                "Library and version lock-in",
                "Generated components are tightly coupled to specific library versions and "
                "Tailwind conventions. Integrating them into an existing design system, or "
                "upgrading a dependency, breaks things in ways that aren't obvious from the "
                "diff.",
            ),
        ],
        "faq": [
            (
                "My v0 components look done but nothing actually works. What's wrong?",
                "Almost always missing backend wiring &mdash; v0 built the UI, not the API "
                "routes or database logic behind it. That's the first thing I check.",
            ),
            (
                "Can you integrate v0 components into our existing app?",
                "Yes. That's routine work &mdash; reconciling library versions, Tailwind "
                "config, and design system conventions so the generated pieces actually fit.",
            ),
            (
                "Do you review v0 output for security issues?",
                "Yes. Polished UI is exactly why AI-generated components get shipped "
                "without a security pass &mdash; I do that pass as part of the diagnostic.",
            ),
            (
                "Is v0 a bad tool to use?",
                "No &mdash; it's a fast way to get UI scaffolding. It's just not a complete "
                "app builder. Keep using it for what it's good at; I handle the rest.",
            ),
        ],
    },
}

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tagline} | AI App Rescue Service</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://ifixyour.app/fix/{slug}/">

    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">

    <meta property="og:title" content="{tagline}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://ifixyour.app/fix/{slug}/">
    <meta property="og:image" content="https://ifixyour.app/og-image.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{tagline}">
    <meta name="twitter:description" content="{meta_desc}">
    <meta name="twitter:image" content="https://ifixyour.app/og-image.jpg">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600;700;900&display=swap" rel="stylesheet">

    <script type="application/ld+json">
    {service_jsonld}
    </script>
    <script type="application/ld+json">
    {faq_jsonld}
    </script>
    <script type="application/ld+json">
    {breadcrumb_jsonld}
    </script>

    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                        display: ['DM Serif Display', 'Georgia', 'serif'],
                    }},
                    colors: {{
                        dark: '#1B1B2F',
                        darker: '#141425',
                        surface: '#252540',
                        accent: '#E8A838',
                        'accent-dim': '#D4952E',
                        muted: '#9B9BB0',
                        light: '#F0EDE8',
                        border: '#2E2E48',
                    }}
                }}
            }}
        }}
    </script>
    <style>
        html {{ scroll-behavior: smooth; }}
    </style>
</head>
<body class="bg-darker text-light font-sans">

    <!-- Nav -->
    <nav class="px-6 py-8 max-w-6xl mx-auto flex justify-between items-center">
        <a href="/" class="font-bold text-xl tracking-tight text-white">ifixyour.app</a>
        <a href="#apply" class="text-sm font-semibold text-accent hover:text-accent-dim tracking-wide uppercase transition-colors">Get a diagnostic &rarr;</a>
    </nav>

    <!-- Breadcrumb -->
    <div class="px-6 max-w-6xl mx-auto">
        <nav aria-label="Breadcrumb" class="text-sm text-muted">
            <a href="/" class="hover:text-accent transition-colors">Home</a>
            <span class="mx-2">/</span>
            <span class="text-light">Fix {name}</span>
        </nav>
    </div>
"""

FOOTER = """
    <script>
    const form = document.getElementById('apply-form');
    const btn = form.querySelector('button[type="submit"]');
    const status = document.getElementById('form-status');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      btn.disabled = true;
      btn.textContent = 'Submitting...';
      status.classList.add('hidden');

      const data = Object.fromEntries(new FormData(form));

      try {
        const res = await fetch('https://ifixyourapp-api.winslowcj5.workers.dev/submit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data),
        });

        if (res.ok) {
          form.reset();
          status.textContent = "Application received. I'll review it within 48 hours.";
          status.className = 'text-center py-4 text-lg font-semibold text-green-400';
        } else {
          const err = await res.json();
          throw new Error(err.error || 'Submission failed');
        }
      } catch (e) {
        status.textContent = 'Something went wrong. Email hello@ifixyour.app instead.';
        status.className = 'text-center py-4 text-lg font-semibold text-red-400';
      } finally {
        btn.disabled = false;
        btn.textContent = 'Submit Application';
      }
    });
    </script>

    <!-- Footer -->
    <footer class="px-6 py-16 border-t border-border">
        <div class="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
            <a href="/" class="font-bold text-xl tracking-tight text-white">ifixyour.app</a>
            <a href="mailto:hello@ifixyour.app" class="text-muted hover:text-accent transition-colors">hello@ifixyour.app</a>
        </div>
    </footer>

</body>
</html>
"""


def failure_html(failures):
    items = []
    for title, body in failures:
        items.append(
            f'<div>\n'
            f'                <h3 class="text-xl font-bold text-white mb-3">{title}</h3>\n'
            f'                <p class="text-muted text-lg leading-relaxed">{body}</p>\n'
            f'            </div>'
        )
    return "\n\n            ".join(items)


def faq_html(faq):
    items = []
    for q, a in faq:
        items.append(
            f'<div>\n'
            f'                <h3 class="font-display text-xl text-white mb-3">{q}</h3>\n'
            f'                <p class="text-muted text-lg">{a}</p>\n'
            f'            </div>'
        )
    return "\n            ".join(items)


def service_jsonld(tool):
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": f"{tool['name']} App Repair",
            "name": f"Fix Your {tool['name']} App",
            "url": f"https://ifixyour.app/fix/{tool['slug']}/",
            "description": tool["meta_desc"],
            "provider": {
                "@type": "ProfessionalService",
                "name": "I Fix Your App",
                "url": "https://ifixyour.app",
                "founder": {"@type": "Person", "name": "CJ Winslow"},
            },
            "areaServed": "Worldwide",
            "offers": {
                "@type": "AggregateOffer",
                "priceCurrency": "USD",
                "lowPrice": "2500",
                "highPrice": "25000",
            },
        },
        indent=2,
    )


def faq_jsonld(tool):
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a.replace("&mdash;", "-")},
                }
                for q, a in tool["faq"]
            ],
        },
        indent=2,
    )


def breadcrumb_jsonld(tool):
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://ifixyour.app/"},
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": f"Fix {tool['name']}",
                    "item": f"https://ifixyour.app/fix/{tool['slug']}/",
                },
            ],
        },
        indent=2,
    )


PAGE_BODY = """
    <!-- Hero -->
    <section class="px-6 pt-16 pb-28 max-w-6xl mx-auto">
        <h1 class="font-display text-5xl md:text-7xl lg:text-8xl leading-[0.95] tracking-tight text-white mb-10 max-w-4xl">
            Your {name} app<br>is broken.<br>
            <span class="italic text-accent">I fix it.</span>
        </h1>
        <p class="text-xl text-muted max-w-2xl leading-relaxed mb-12">{intro}</p>
        <a href="#apply" class="inline-block bg-accent text-darker font-bold px-10 py-5 text-lg tracking-tight hover:bg-accent-dim transition-colors">
            Apply for free diagnostic
        </a>
    </section>

    <div class="h-px bg-accent/20 max-w-6xl mx-auto"></div>

    <!-- Failure modes -->
    <section class="px-6 py-28 max-w-6xl mx-auto">
        <p class="text-xs font-semibold text-accent tracking-[0.3em] uppercase mb-8">/01 What Breaks</p>
        <h2 class="font-display text-4xl md:text-6xl tracking-tight text-white mb-16 max-w-3xl">
            {name} failure modes I see every week.
        </h2>
        <div class="grid md:grid-cols-2 gap-x-16 gap-y-14 max-w-5xl">
            {failures}
        </div>
    </section>

    <div class="h-px bg-border max-w-6xl mx-auto"></div>

    <!-- How it works -->
    <section class="px-6 py-28 max-w-6xl mx-auto">
        <p class="text-xs font-semibold text-accent tracking-[0.3em] uppercase mb-8">/02 How It Works</p>
        <h2 class="font-display text-4xl md:text-6xl tracking-tight text-white mb-20">Stupidly simple.</h2>
        <div class="space-y-20 max-w-3xl">
            <div class="flex gap-10 items-start">
                <span class="text-6xl font-display text-accent/40 shrink-0 leading-none">1</span>
                <div>
                    <h3 class="text-2xl font-bold text-white mb-3">You tell me what's broken</h3>
                    <p class="text-muted text-lg">Fill out the form. Share your repo or describe the symptoms. Takes 2 minutes.</p>
                </div>
            </div>
            <div class="flex gap-10 items-start">
                <span class="text-6xl font-display text-accent/40 shrink-0 leading-none">2</span>
                <div>
                    <h3 class="text-2xl font-bold text-white mb-3">I diagnose it (free)</h3>
                    <p class="text-muted text-lg">30-minute call where I've already looked at your {name} code. You get a clear assessment: what's wrong, what it costs to fix, how long it takes.</p>
                </div>
            </div>
            <div class="flex gap-10 items-start">
                <span class="text-6xl font-display text-accent/40 shrink-0 leading-none">3</span>
                <div>
                    <h3 class="text-2xl font-bold text-white mb-3">I fix it</h3>
                    <p class="text-muted text-lg">You approve the flat-fee quote. I get to work. Most rescues ship in 1-2 weeks.</p>
                </div>
            </div>
        </div>
    </section>

    <div class="h-px bg-border max-w-6xl mx-auto"></div>

    <!-- Pricing -->
    <section class="px-6 py-28 max-w-6xl mx-auto">
        <p class="text-xs font-semibold text-accent tracking-[0.3em] uppercase mb-8">/03 Pricing</p>
        <h2 class="font-display text-4xl md:text-6xl tracking-tight text-white mb-6">Flat fees. No hourly BS.</h2>
        <p class="text-lg text-muted mb-20 max-w-xl">You know the cost before I start. No scope creep surprises.</p>

        <div class="space-y-0">
            <div class="border-b border-border py-12">
                <div class="flex flex-col md:flex-row md:items-baseline md:justify-between mb-4 gap-2">
                    <h3 class="font-display text-2xl text-white">Triage</h3>
                    <span class="text-4xl font-bold text-accent">$2,500</span>
                </div>
                <p class="text-muted text-lg">One critical issue diagnosed and fixed. 48-hour turnaround.</p>
            </div>
            <div class="border-b border-border py-12">
                <div class="flex flex-col md:flex-row md:items-baseline md:justify-between mb-4 gap-2">
                    <h3 class="font-display text-2xl text-white">Stabilize</h3>
                    <span class="text-4xl font-bold text-accent">$5,000 &ndash; $10,000</span>
                </div>
                <p class="text-muted text-lg">Fix all critical bugs. Get deploys working. Make it reliable. 1-2 weeks.</p>
            </div>
            <div class="border-b border-border py-12">
                <div class="flex flex-col md:flex-row md:items-baseline md:justify-between mb-4 gap-2">
                    <h3 class="font-display text-2xl text-white">Rebuild Right</h3>
                    <span class="text-4xl font-bold text-accent">$15,000 &ndash; $25,000</span>
                </div>
                <p class="text-muted text-lg">Re-architect the broken parts properly. CI/CD, testing, monitoring. 2-4 weeks.</p>
            </div>
        </div>
    </section>

    <div class="h-px bg-border max-w-6xl mx-auto"></div>

    <!-- FAQ -->
    <section class="px-6 py-28 max-w-6xl mx-auto">
        <p class="text-xs font-semibold text-accent tracking-[0.3em] uppercase mb-8">/04 Questions</p>
        <div class="space-y-14 max-w-3xl">
            {faq}
        </div>
    </section>

    <div class="h-px bg-accent/20 max-w-6xl mx-auto"></div>

    <!-- Apply -->
    <section id="apply" class="px-6 py-28 max-w-3xl mx-auto">
        <p class="text-xs font-semibold text-accent tracking-[0.3em] uppercase mb-8">/05 Apply</p>
        <h2 class="font-display text-4xl md:text-6xl tracking-tight text-white mb-4">Get a free diagnostic.</h2>
        <p class="text-lg text-muted mb-14">30 minutes. I review your {name} app before the call and come with specific observations. No pitch deck, no sales team.</p>

        <form id="apply-form" class="space-y-6">
            <div class="grid md:grid-cols-2 gap-4">
                <div>
                    <label for="name" class="block text-sm font-medium text-muted mb-2 uppercase tracking-wide">Name</label>
                    <input type="text" id="name" name="name" required
                        class="w-full border border-border bg-surface text-white px-4 py-4 focus:border-accent focus:ring-2 focus:ring-accent/20 focus:outline-none transition-all placeholder-muted/50">
                </div>
                <div>
                    <label for="email" class="block text-sm font-medium text-muted mb-2 uppercase tracking-wide">Work email</label>
                    <input type="email" id="email" name="email" required
                        class="w-full border border-border bg-surface text-white px-4 py-4 focus:border-accent focus:ring-2 focus:ring-accent/20 focus:outline-none transition-all placeholder-muted/50">
                </div>
            </div>
            <div>
                <label for="company" class="block text-sm font-medium text-muted mb-2 uppercase tracking-wide">Company</label>
                <input type="text" id="company" name="company"
                    class="w-full border border-border bg-surface text-white px-4 py-4 focus:border-accent focus:ring-2 focus:ring-accent/20 focus:outline-none transition-all placeholder-muted/50">
            </div>
            <div>
                <label for="app_url" class="block text-sm font-medium text-muted mb-2 uppercase tracking-wide">App URL or repo link</label>
                <input type="text" id="app_url" name="app_url" placeholder="https://..."
                    class="w-full border border-border bg-surface text-white px-4 py-4 focus:border-accent focus:ring-2 focus:ring-accent/20 focus:outline-none transition-all placeholder-muted/50">
            </div>
            <div class="grid md:grid-cols-2 gap-4">
                <div>
                    <label for="revenue" class="block text-sm font-medium text-muted mb-2 uppercase tracking-wide">Monthly revenue</label>
                    <select id="revenue" name="revenue"
                        class="w-full border border-border bg-surface text-white px-4 py-4 focus:border-accent focus:ring-2 focus:ring-accent/20 focus:outline-none transition-all">
                        <option value="pre-revenue">Pre-revenue (funded)</option>
                        <option value="under-10k">Under $10k/mo</option>
                        <option value="10k-50k">$10k-$50k/mo</option>
                        <option value="50k-plus">$50k+/mo</option>
                    </select>
                </div>
                <div>
                    <label for="users" class="block text-sm font-medium text-muted mb-2 uppercase tracking-wide">Active users</label>
                    <select id="users" name="users"
                        class="w-full border border-border bg-surface text-white px-4 py-4 focus:border-accent focus:ring-2 focus:ring-accent/20 focus:outline-none transition-all">
                        <option value="under-100">Under 100</option>
                        <option value="100-1000">100-1,000</option>
                        <option value="1000-10000">1,000-10,000</option>
                        <option value="10000-plus">10,000+</option>
                    </select>
                </div>
            </div>
            <div>
                <label for="description" class="block text-sm font-medium text-muted mb-2 uppercase tracking-wide">What's broken?</label>
                <textarea id="description" name="description" rows="4" required
                    class="w-full border border-border bg-surface text-white px-4 py-4 focus:border-accent focus:ring-2 focus:ring-accent/20 focus:outline-none transition-all placeholder-muted/50"
                    placeholder="What's failing, what users see, how long it's been like this..."></textarea>
            </div>
            <div>
                <label for="urgency" class="block text-sm font-medium text-muted mb-2 uppercase tracking-wide">Urgency</label>
                <select id="urgency" name="urgency"
                    class="w-full border border-border bg-surface text-white px-4 py-4 focus:border-accent focus:ring-2 focus:ring-accent/20 focus:outline-none transition-all">
                    <option value="medium" selected>Standard - this week</option>
                    <option value="high">Urgent - app is degraded</option>
                    <option value="critical">Emergency - app is down now</option>
                </select>
            </div>
            <button type="submit"
                class="w-full bg-accent text-darker font-bold py-5 text-lg tracking-tight hover:bg-accent-dim transition-colors">
                Submit Application
            </button>
            <p class="text-sm text-muted text-center">I review every application within 48 hours.</p>
            <div id="form-status" class="hidden text-center py-4 text-lg font-semibold"></div>
        </form>
    </section>
"""


def build():
    fix_dir = os.path.join(ROOT, "fix")
    for slug, tool in TOOLS.items():
        tool["slug"] = slug
        page_dir = os.path.join(fix_dir, slug)
        os.makedirs(page_dir, exist_ok=True)

        html = HEAD.format(
            tagline=tool["tagline"],
            meta_desc=tool["meta_desc"],
            slug=slug,
            name=tool["name"],
            service_jsonld=service_jsonld(tool),
            faq_jsonld=faq_jsonld(tool),
            breadcrumb_jsonld=breadcrumb_jsonld(tool),
        )
        html += PAGE_BODY.format(
            name=tool["name"],
            intro=tool["intro"],
            failures=failure_html(tool["failures"]),
            faq=faq_html(tool["faq"]),
        )
        html += FOOTER

        out_path = os.path.join(page_dir, "index.html")
        with open(out_path, "w") as f:
            f.write(html)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    build()
