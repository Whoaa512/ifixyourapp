export interface Env {
  DB: D1Database;
  TELNYX_API_KEY: string;
  TELNYX_FROM_NUMBER: string;
  NOTIFY_PHONE: string;
}

interface Submission {
  name: string;
  email: string;
  company?: string;
  app_url?: string;
  revenue?: string;
  users?: string;
  description: string;
  urgency?: string;
}

const ALLOWED_ORIGINS = [
  "https://ifixyour.app",
  "http://localhost:8888",
];

function corsHeaders(origin?: string | null): Record<string, string> {
  const allowed = origin && ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    "Access-Control-Allow-Origin": allowed,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };
}

function json(data: object, status: number, origin?: string | null): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json", ...corsHeaders(origin) },
  });
}

async function sendSms(env: Env, submission: Submission): Promise<boolean> {
  const urgencyTag =
    submission.urgency === "critical"
      ? "EMERGENCY"
      : submission.urgency === "high"
        ? "URGENT"
        : "";

  const text = [
    `New lead: ${submission.name}`,
    submission.company ? `Company: ${submission.company}` : null,
    `Email: ${submission.email}`,
    urgencyTag ? `[${urgencyTag}]` : null,
    submission.description.substring(0, 120),
  ]
    .filter(Boolean)
    .join("\n");

  const res = await fetch("https://api.telnyx.com/v2/messages", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.TELNYX_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: env.TELNYX_FROM_NUMBER,
      to: `+1${env.NOTIFY_PHONE}`,
      text,
    }),
  });

  return res.ok;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const origin = request.headers.get("Origin");

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }

    const url = new URL(request.url);
    if (request.method !== "POST" || url.pathname !== "/submit") {
      return json({ error: "Not found" }, 404, origin);
    }

    let data: Submission;
    try {
      data = await request.json();
    } catch {
      return json({ error: "Invalid JSON" }, 400, origin);
    }

    if (!data.name || !data.email || !data.description) {
      return json({ error: "name, email, and description are required" }, 400, origin);
    }

    const result = await env.DB.prepare(
      `INSERT INTO submissions (name, email, company, app_url, revenue, users, description, urgency)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)`
    )
      .bind(
        data.name,
        data.email,
        data.company || null,
        data.app_url || null,
        data.revenue || null,
        data.users || null,
        data.description,
        data.urgency || "medium"
      )
      .run();

    let smsSent = false;
    try {
      smsSent = await sendSms(env, data);
    } catch (e) {
      console.error("SMS failed:", e);
    }

    if (smsSent && result.meta.last_row_id) {
      await env.DB.prepare("UPDATE submissions SET sms_sent = 1 WHERE id = ?")
        .bind(result.meta.last_row_id)
        .run();
    }

    return json({ success: true }, 200, origin);
  },
};
