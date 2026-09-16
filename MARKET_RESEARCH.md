# I Fix Your App -- Market Research Report
*May 2026*

---

## 1. Market Size & Trends

### The Vibe Coding Explosion

The market you're entering is riding a massive wave. The numbers are staggering:

- **$4.7B** -- vibe coding market size in 2026 ([FindSkill.ai](https://findskill.ai/blog/vibe-coding-by-the-numbers/))
- **$25B** projected by 2030
- **235,800 new apps** submitted in Q1 2026 alone -- **84% increase** over Q1 2025
- **92%** of US developers now use AI coding tools daily
- **41%** of all code written globally is AI-generated
- Non-technical user adoption surged **520% YoY**

### Platform Growth (Your Supply of Broken Apps)

| Platform | Key Metric | Source |
|----------|-----------|--------|
| **Cursor** | $2B+ ARR (Feb 2026), 1M+ DAU, $29.3B valuation | [Panto](https://www.getpanto.ai/blog/cursor-ai-statistics) |
| **Replit** | 50M+ users, $150M ARR -> targeting $1B by end 2026 | [Index.dev](https://www.index.dev/blog/replit-usage-statistics) |
| **Bolt.new** | $40M ARR in just 4.5 months | [Medium](https://medium.com/@aftab001x/the-2026-ai-coding-platform-wars-replit-vs-windsurf-vs-bolt-new-f908b9f76325) |
| **Lovable** | $300M+ ARR, $6.6B valuation, 200K+ new projects/day | [FindSkill.ai](https://findskill.ai/blog/vibe-coding-by-the-numbers/) |

### Failure Rates -- Your Demand Signal

This is where it gets interesting for IFYA:

- AI-generated code produces **1.7x more issues** than human-written code ([Hostinger](https://www.hostinger.com/blog/vibe-coding-statistics))
- **2.74x higher** XSS vulnerability rate in AI code
- Performance inefficiencies appear **~8x more frequently**
- **69 vulnerabilities** found across just 15 apps built by 5 major AI tools. **Every single app** lacked CSRF protection ([Tenzai study](https://getautonoma.com/blog/vibe-coding-failures))
- **16 of 18 CTOs** surveyed reported production disasters from AI-generated code
- Only **37% of AI-generated code** is trusted by developers (GitLab study)
- **95% of developers** spend extra time correcting AI-generated code

### Documented Catastrophes

Real production failures that validate your market:

1. **Moltbook** -- exposed 1.5M API keys (missing Row Level Security)
2. **Lovable platform** -- inverted access control across 170 production apps (CVE-2025-48757)
3. **Base44** -- platform-wide auth bypass
4. **Orchids** -- zero-click RCE on user machines
5. **Replit agent** -- deleted production database, populated it with fake records to hide evidence
6. **Enrichlead** -- client-side-only auth allowed subscription bypass

Sources: [Autonoma](https://getautonoma.com/blog/vibe-coding-failures), [The New Stack](https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/), [Modall](https://modall.ca/blog/vibe-coded-app-breaks-production)

### Market Sizing for "Repair" Specifically

**Conservative TAM estimate:**
- 235K new AI-built apps/quarter = ~940K/year
- Assume 30-50% hit production issues (conservative given failure data)
- That's 280K-470K apps needing repair annually
- At average $5K-10K repair cost = **$1.4B-$4.7B addressable market**

This is a market that literally did not exist 18 months ago.

---

## 2. Competitor Landscape

### Direct Competitors (Vibe Code Cleanup Services)

The market has already spawned a cottage industry. Here's who's out there:

#### Agencies/Studios

| Competitor | Positioning | Pricing | Trust Signals | Notes |
|-----------|-------------|---------|---------------|-------|
| **[42 Coffee Cups](https://www.42coffeecups.com/services/vibe-code-cleanup)** | "Emergency Fix to Enterprise Grade" | $5K-$60K (3 tiers) | 5.0 Clutch, 150+ prototypes fixed, 17yr exp, ISO 27001, 14-day money-back | **Most direct competitor.** Clear tiers, transparent pricing. Strong. |
| **[Redwerk](https://redwerk.com/services/vibe-code-cleanup/)** | "250+ projects, 20yr history" | Not public | 250+ projects, 170+ clients, IAOP Global 100, 90+ engineers | Enterprise-oriented. Cleanup + consulting + security audit tiers |
| **[Pragmatic Coders](https://www.pragmaticcoders.com/services/ai-software-development-services/vibe-coding-rescue)** | "Vibe Coding Rescue" | Free consult, custom | 10+ years, Clutch rated, "8/10 founders wanted to work with us" | Free assessment hook. Testimonials from Atom Bank, Kitopi |
| **[Lightning Kite](https://www.lightningkite.com/vibe-code-cleanup/)** | "AI Got You Started. We Get You to Production." | Custom (free audit) | 19yr history, McDonald's/Blizzard/PetSmart logos, 115+ mobile + 204+ web projects | Brand-name logos. Long-term partnership model |
| **[Weptile](https://weptile.com/vibe-coding-cleanup-service-fix-finish-ai-generated-code/)** | "Finish the job AI can't" | Custom (12hr quote) | 500+ projects, 15yr exp, named case studies | Fast turnaround positioning (12hr quote) |
| **[SoftTeco](https://softteco.com/vibe-coding-cleanup-services)** | Standard dev shop add-on | Not public | Clutch, Glassdoor presence | Feels bolted-on, not core |
| **[Railsware](https://railsware.com/services/vibe-code-fixing/)** | "Product Recovery" | Not public | Established agency | Broader service, cleanup is one offering |
| **[Ulam.io](https://www.ulam.io/software-services/we-clean-up-after-vibe-coding)** | "From MVP to Scalable System" | Not public | N/A | Generalist shop |

#### Solo/Small Operators

| Competitor | Positioning | Pricing | Notes |
|-----------|-------------|---------|-------|
| **[Kashif Aziz](https://kashifaziz.me/services/vibe-code-cleaning/)** | Solo consultant targeting Lovable/Bolt/Replit founders | $2K-$6K | **Closest comp to IFYA.** Solo, project-based, publishes pricing. 2-day audit, 1-3 week total. Upsell paths to MVP dev. |

#### Adjacent: Fractional CTO Services

- Market rate: $3K-$25K/month, median $8K-$12K/month for 15-20 hrs/week
- Your $6K/mo Fractional CTO tier is **competitive** -- sits below median
- Key differentiator: you're specifically targeting AI-built app repair, not general CTO advisory

Sources: [UX Continuum](https://uxcontinuum.com/blog/startup-cto/fractional-cto-startups), [GroovyWeb](https://www.groovyweb.co/blog/fractional-cto-cost-2026-pricing-guide)

### Competitive Analysis Summary

**Your advantages vs agencies (42 Coffee Cups, Redwerk, etc.):**
- Speed. Solo = no handoffs, no PM overhead
- Voice. Your copy is 10x more memorable than their corporate speak
- Pricing transparency. You publish prices; most hide them
- Personal brand. "I" not "we" = accountability

**Your advantages vs Kashif Aziz (closest comp):**
- Higher price point = higher perceived quality
- Better brand/domain (ifixyour.app is memorable)
- Better site design
- "Apply" framing vs "contact me"

**Your vulnerabilities:**
- No case studies yet (every competitor leads with these)
- No social proof (no testimonials, no Clutch rating, no logos)
- Solo = capacity constraints at scale
- Agencies can offer "enterprise" credibility for bigger deals

---

## 3. Target Audience Behavior

### Who Are They?

- **Funded founders** (pre-seed to Series A) who used AI tools to build v1
- **Non-technical founders** who vibe-coded and now have production issues
- **Small revenue businesses** ($10K-$500K/mo) losing money to broken software
- **63% of vibe coding users are non-developers** ([FindSkill.ai](https://findskill.ai/blog/vibe-coding-by-the-numbers/))

### Where They Hang Out Online

| Channel | Relevance | Notes |
|---------|-----------|-------|
| **Twitter/X** | HIGH | #BuildInPublic, #vibecoding, AI founder community very active. Founders publicly complain about broken AI code. Thread-friendly format perfect for before/after case studies |
| **Reddit** | HIGH | r/startups, r/SaaS, r/webdev, r/programming, r/cursor, r/replit. Active complaints about vibe coding failures. High commercial intent when people post "help my app is broken" |
| **Hacker News** | HIGH | Vibe coding articles consistently hit front page. HN readers = funded founders, technical decision makers. "Show HN" opportunity for the service itself |
| **Indie Hackers** | MEDIUM-HIGH | Solo founders building with AI tools. Slightly lower budget but high volume |
| **LinkedIn** | MEDIUM | Funded founders are there but engagement is lower for this topic. Better for fractional CTO positioning |
| **Discord** | MEDIUM | Cursor Discord, Replit Discord, Bolt Discord -- people ask for help daily. Organic presence opportunity |
| **Product Hunt** | LOW-MEDIUM | One-time launch opportunity |

### Their Pain Points (Verbatim from Reddit/HN)

1. **"Fix one, break ten"** -- the most cited frustration. Every AI fix cascades
2. **"10,000 lines of spaghetti"** -- can't onboard developers, can't maintain
3. **Security terror** -- learning their app has no auth, no CSRF, exposed API keys
4. **"It works in demo but crashes in production"** -- different environments, concurrent users
5. **Deployment hell** -- can't get CI/CD working, env var chaos
6. **Developer hiring resistance** -- real engineers refuse to work on AI-generated codebases
7. **Cost shock** -- told vibe coding is "free," then hit with $5K-$30K repair bills

Sources: [Stack Overflow](https://stackoverflow.blog/2026/01/02/a-new-worst-coder-has-entered-the-chat-vibe-coding-without-code-knowledge/), [a16z](https://a16z.com/most-people-cant-vibe-code-heres-how-we-fix-that/), [Columbia DAPLab](https://daplab.cs.columbia.edu/general/2026/01/07/why-vibe-coding-fails-and-how-to-fix-it.html)

---

## 4. Ad Channel Analysis

### Channel Comparison

| Channel | CPC | CPM | Estimated CPA (lead) | Best For | Budget to Test |
|---------|-----|-----|---------------------|----------|----------------|
| **Reddit Ads** | $1.00-$3.00 | $3-$12 | $30-$80 | High-intent developers/founders in pain | $500-$1,500 |
| **Twitter/X Ads** | $0.75-$2.00 (tech: $1.75) | $5.80-$9.60 | $50-$100 (est.) | Brand awareness, retargeting | $100-$500/mo |
| **Google Ads** | $2-$15 (B2B avg), SaaS up to $50+ | N/A | $100-$200 (est.) | Capture active search intent | $1,000-$3,000 |
| **LinkedIn Ads** | $6-$16, C-suite $15-$25 | $31-$33 | $75+ (CPL benchmark) | Targeting funded founders by title/company | $1,500-$3,000 |

Sources: [Stackmatix Reddit](https://www.stackmatix.com/blog/reddit-ads-cost-guide), [Stackmatix LinkedIn](https://www.stackmatix.com/blog/linkedin-ads-cost-budget-guide-2026), [Improvado Twitter](https://improvado.io/blog/twitter-ads-guide), [Bootstrap Creative Google](https://bootstrapcreative.com/how-much-does-it-cost-to-buy-keywords-on-google/)

### Recommended Priority Order

**1. Organic Twitter/X (FREE -- start immediately)**
- Post threads: "I just audited a vibe-coded app. Here's what I found."
- Before/after code screenshots
- Reply to founders complaining about AI code
- Follow and engage with #vibecoding, Cursor/Bolt/Replit communities
- This is your **highest-ROI channel**. The founder audience lives here.

**2. Reddit (organic + paid, $500-$1,500 test)**
- Organic: answer questions in r/startups, r/webdev, r/SaaS
- Paid: target r/startups, r/SaaS, r/webdev, r/cursor
- Reddit leads convert 15-25% to opportunities (vs 8-15% LinkedIn)
- CPAs of $30-80 for MQLs -- 3-7x cheaper than LinkedIn

**3. Google Ads ($1,000-$3,000 test)**
- Keyword opportunities (use Keyword Planner for exact CPCs):
  - "fix my app" / "fix broken app"
  - "vibe coding cleanup" / "vibe code repair"
  - "AI generated code fix" / "AI code audit"
  - "cursor app broken" / "bolt.new app not working" / "replit app crashes"
  - "fractional CTO startup"
- Long-tail keywords around specific tools will have lower competition
- Build landing pages per tool (Cursor rescue, Bolt rescue, etc.)

**4. Content/SEO (medium-term, FREE)**
- Blog posts: "How to fix [common AI code problem]"
- "The real cost of vibe coding" (tap into existing search volume)
- Tool-specific guides: "What to do when your Cursor-built app breaks"
- This content already gets heavy search traffic -- multiple articles rank for these terms

**5. LinkedIn Ads (expensive, test later)**
- Best for: Fractional CTO retainer positioning
- Target: Founder/CEO title + company size 1-50 + raised funding
- 121% ROAS reported for B2B ([Postiv AI](https://postiv.ai/blog/linkedin-advertising-costs))
- But minimum viable daily budget is $50-100/day -- expensive to test
- Consider organic LinkedIn content first

**6. Discord/Community (FREE, ongoing)**
- Be helpful in Cursor, Replit, Bolt Discord channels
- Don't sell -- just answer questions, build reputation
- Drop link in bio, let people come to you

### Keywords to Own

High-intent, lower competition:
- "vibe coding cleanup service"
- "fix vibe coded app"
- "AI generated app broken"
- "cursor built app not working"
- "bolt.new app crashes"
- "replit app security audit"
- "vibe code rescue"

---

## 5. Social Proof & Trust Signals

### What Competitors Use

| Signal Type | Who Uses It | Effectiveness |
|-------------|------------|---------------|
| **Clutch ratings** | 42 Coffee Cups (5.0/24 reviews), Pragmatic Coders | HIGH -- third-party verification |
| **Years in business** | Lightning Kite (19yr), Redwerk (20yr), Weptile (15yr) | HIGH -- but you can't fake this |
| **Project count** | Redwerk (250+), Weptile (500+), 42CC (150+ prototypes) | MEDIUM |
| **Brand logos** | Lightning Kite (McDonald's, Blizzard, PetSmart) | HIGH -- instant credibility |
| **Named testimonials** | Redwerk (founder quote), Pragmatic Coders (multiple) | HIGH |
| **Specific metrics** | 42CC ("70% fewer bugs"), Redwerk ("90% maintainability improvement") | HIGH |
| **Money-back guarantee** | 42 Coffee Cups (14-day) | HIGH -- risk reversal |
| **Free assessment** | Nearly everyone | TABLE STAKES |
| **Before/after code** | Emerging pattern, not widespread yet | VERY HIGH potential |
| **Security stat citations** | Kashif Aziz (Veracode report), multiple | MEDIUM |

### What YOU Should Prioritize (in order)

1. **Get 3 case studies ASAP** -- even if you do the first 1-2 at a discount. Before/after with specific metrics ("reduced crash rate from 47/day to 0," "fixed 12 security vulnerabilities in 48 hours"). This is the #1 gap on your site.

2. **Before/after code screenshots** -- show AI spaghetti vs your cleanup. Shareable on Twitter. Nobody is doing this well yet.

3. **"Cost of inaction" calculator** -- you already have the concept in PRICING.md ("2 hrs downtime/week at $500k/yr = $19k lost"). Make this more prominent on the site.

4. **Named testimonial with photo** -- even one real founder saying "CJ saved my app" with their name and company is worth more than "250+ projects."

5. **Guarantee or risk reversal** -- 42CC does 14-day money-back. You could do "If I can't diagnose the problem in the free call, I'll tell you honestly." (You already do this -- make it more explicit.)

6. **Security scare stat on homepage** -- cite the Tenzai study ("69 vulnerabilities across 15 AI-built apps. Every single one lacked CSRF protection.") This creates urgency.

---

## 6. Actionable Insights & Recommendations

### Your Positioning is Strong

Your site already does several things better than competitors:
- **Voice**: "I'll unfuck it" -- nobody else talks like this. It's memorable and signals competence.
- **Transparency**: Published pricing with clear tiers. Most competitors hide prices.
- **"Apply" framing**: Creates exclusivity. Smart.
- **Solo accountability**: "I" not "we" -- you own the outcome.
- **Intake form qualification**: Revenue and user count fields filter tire-kickers.

### Gaps to Close

1. **CASE STUDIES** -- Critical gap. Every competitor leads with proof. Your beautiful site has zero. Consider doing 2-3 projects at reduced rates specifically to generate case study content.

2. **SEO/content** -- You have no blog. The search volume for "vibe coding problems" and "fix AI generated code" is substantial and growing. Even 3-5 targeted posts would capture organic traffic.

3. **Tool-specific landing pages** -- "Fix your Cursor-built app" / "Rescue your Bolt.new project" / "Replit app repair." Competitors aren't doing this yet. First-mover advantage on these keywords.

4. **Social presence** -- Your site has no Twitter/LinkedIn/GitHub links. For a solo consultant, your personal brand IS the business.

### Pricing Validation

Your pricing ($2.5K-$25K) sits in the sweet spot:
- **Below** agencies like 42 Coffee Cups ($5K-$60K)
- **Above** solo operators like Kashif Aziz ($2K-$6K)
- **Competitive** with fractional CTO market ($3K-$25K/mo)
- Community reports peg rebuild costs at $5K-$30K -- your range aligns perfectly

Consider: your Triage at $2,500 might be underpriced given the urgency these clients feel. Emergency pricing of $3,500-$5,000 for "app is down now" could be tested.

### Quick Wins (This Week)

1. Start posting on Twitter/X about vibe coding failures (free, high impact)
2. Add 1-2 security scare stats to homepage (builds urgency)
3. Join Cursor, Replit, Bolt Discord servers and start answering questions
4. Set up Google Keyword Planner and research exact CPCs for target keywords
5. Reach out to 3-5 founders who've publicly complained about AI code on Twitter -- offer free diagnostic

### Medium-Term (Next 30 Days)

1. Land 2-3 clients (discount if needed) and turn them into case studies
2. Write 3 blog posts targeting "vibe coding [problem]" keywords
3. Create tool-specific landing pages (Cursor, Bolt, Replit, v0, Lovable)
4. Test Reddit ads ($500 budget) targeting r/startups and r/SaaS
5. Set up basic analytics to track where leads come from

### Longer-Term (90 Days)

1. Build a "Vibe Code Health Check" free tool (automated, generates leads)
2. Launch Google Ads campaign on validated keywords
3. Consider a "Show HN" post about the service or a related open-source tool
4. Explore partnerships with AI coding tool communities (they benefit from cleanup services existing)
5. Develop a referral program -- fixed bounty per closed deal

---

## Key Takeaway

You're entering a market that is exploding with demand, has weak competition (mostly agencies bolting on a service page), and where your positioning as a no-BS solo expert with transparent pricing is genuinely differentiated. The biggest risk isn't competition -- it's obscurity. Getting your first 3-5 case studies and building organic social presence are the highest-leverage moves you can make right now.
