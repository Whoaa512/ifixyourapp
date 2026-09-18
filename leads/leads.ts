// Local leads dashboard + iMessage notifier for ifixyourapp form submissions.
// Polls D1 via wrangler, texts cj on new rows, serves a dashboard on :7777.

import { readFileSync, writeFileSync } from "fs";

const WORKER_DIR = new URL("../worker", import.meta.url).pathname;
const WRANGLER_BIN = new URL("../worker/node_modules/.bin/wrangler", import.meta.url).pathname;
const STATE_PATH = new URL("./state.json", import.meta.url).pathname;
const NOTIFY_NUMBER = "+16263216391";
const DASHBOARD_BASE = "https://airbook.polydactyl-pinecone.ts.net";
const POLL_MS = 60_000;
const PORT = 7777;

interface Submission {
  id: number;
  name: string;
  email: string;
  company: string | null;
  app_url: string | null;
  revenue: string | null;
  users: string | null;
  description: string;
  urgency: string;
  created_at: string;
  sms_sent: number;
}

interface State {
  lastSeenId: number;
}

function loadState(): State {
  try {
    return JSON.parse(readFileSync(STATE_PATH, "utf8"));
  } catch {
    return { lastSeenId: 0 };
  }
}

function saveState(state: State) {
  writeFileSync(STATE_PATH, JSON.stringify(state, null, 2));
}

let cache: Submission[] = [];
let state = loadState();

async function fetchSubmissions(): Promise<Submission[]> {
  const proc = Bun.spawn(
    [
      WRANGLER_BIN,
      "d1",
      "execute",
      "ifixyourapp-submissions",
      "--remote",
      "--json",
      "--command",
      "select * from submissions order by id asc",
    ],
    { cwd: WORKER_DIR, stdout: "pipe", stderr: "pipe" },
  );
  const [stdout, stderr, exitCode] = await Promise.all([
    new Response(proc.stdout).text(),
    new Response(proc.stderr).text(),
    proc.exited,
  ]);
  if (exitCode !== 0) {
    throw new Error(`wrangler exited ${exitCode}: ${stderr}`);
  }
  const parsed = JSON.parse(stdout);
  return parsed[0]?.results ?? [];
}

function escapeAppleScript(str: string): string {
  return str.replace(/\\/g, "\\\\").replace(/"/g, '\\"');
}

async function sendIMessage(body: string): Promise<{ ok: boolean; error?: string }> {
  const script = `
tell application "Messages"
  set targetService to id of 1st service whose service type = iMessage
  set targetBuddy to participant "${NOTIFY_NUMBER}" of service id targetService
  send "${escapeAppleScript(body)}" to targetBuddy
end tell`;
  const proc = Bun.spawn(["osascript", "-e", script], { stdout: "pipe", stderr: "pipe" });
  const [stderr, exitCode] = await Promise.all([new Response(proc.stderr).text(), proc.exited]);
  if (exitCode !== 0) {
    return { ok: false, error: stderr.trim() };
  }
  return { ok: true };
}

function leadMessage(row: Submission): string {
  const snippet = row.description.slice(0, 120);
  return `🚨 New lead: ${row.name} (${row.company ?? "no company"}) — ${row.urgency} — ${snippet}\n${DASHBOARD_BASE}/#${row.id}`;
}

async function poll() {
  let rows: Submission[];
  try {
    rows = await fetchSubmissions();
  } catch (err) {
    console.error(`[poll] fetch failed: ${err}`);
    return;
  }

  cache = rows;
  const newRows = rows.filter((r) => r.id > state.lastSeenId);
  if (newRows.length === 0) return;

  for (const row of newRows) {
    const result = await sendIMessage(leadMessage(row));
    if (!result.ok) {
      console.error(`[imessage] failed for id=${row.id}: ${result.error}`);
      continue;
    }
    console.log(`[imessage] sent for id=${row.id}`);
  }

  state.lastSeenId = Math.max(...rows.map((r) => r.id));
  saveState(state);
}

function urgencyBadge(urgency: string): string {
  const colors: Record<string, string> = {
    high: "#e5484d",
    medium: "#f5a623",
    low: "#5e6ad2",
  };
  const color = colors[urgency] ?? "#666";
  return `<span style="background:${color};color:#fff;padding:2px 8px;border-radius:4px;font-size:12px;text-transform:uppercase">${urgency}</span>`;
}

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function renderDashboard(): string {
  const rows = [...cache].reverse();
  const rowsHtml = rows
    .map(
      (r) => `
    <tr id="${r.id}">
      <td>${r.id}</td>
      <td>${escapeHtml(r.name)}</td>
      <td>${escapeHtml(r.company ?? "")}</td>
      <td><a href="mailto:${escapeHtml(r.email)}">${escapeHtml(r.email)}</a></td>
      <td>${r.app_url ? `<a href="${escapeHtml(r.app_url)}" target="_blank">${escapeHtml(r.app_url)}</a>` : ""}</td>
      <td>${escapeHtml(r.revenue ?? "")}</td>
      <td>${escapeHtml(r.users ?? "")}</td>
      <td>${urgencyBadge(r.urgency)}</td>
      <td>${escapeHtml(r.created_at)}</td>
      <td>${escapeHtml(r.description)}</td>
    </tr>`,
    )
    .join("");

  return `<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>ifixyourapp leads</title>
<style>
  body { background: #0d0d0f; color: #e4e4e7; font-family: -apple-system, system-ui, sans-serif; padding: 24px; }
  h1 { font-size: 18px; color: #fff; }
  table { border-collapse: collapse; width: 100%; margin-top: 16px; }
  th, td { padding: 8px 12px; text-align: left; border-bottom: 1px solid #27272a; vertical-align: top; font-size: 13px; }
  th { color: #a1a1aa; text-transform: uppercase; font-size: 11px; }
  tr:target { background: #1e1e24; }
  a { color: #7dd3fc; }
  td:last-child { max-width: 400px; white-space: pre-wrap; }
</style>
</head>
<body>
<h1>ifixyourapp leads (${rows.length})</h1>
<table>
<thead><tr>
  <th>ID</th><th>Name</th><th>Company</th><th>Email</th><th>App URL</th>
  <th>Revenue</th><th>Users</th><th>Urgency</th><th>Created</th><th>Description</th>
</tr></thead>
<tbody>${rowsHtml}</tbody>
</table>
</body>
</html>`;
}

Bun.serve({
  port: PORT,
  hostname: "0.0.0.0",
  fetch(req) {
    const url = new URL(req.url);
    if (url.pathname === "/") {
      return new Response(renderDashboard(), { headers: { "content-type": "text/html" } });
    }
    return new Response("not found", { status: 404 });
  },
});

console.log(`[leads] serving on :${PORT}, polling every ${POLL_MS / 1000}s`);
poll();
setInterval(poll, POLL_MS);
