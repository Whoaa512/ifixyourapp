# Human TODO

Tasks requiring manual action.

## Telnyx 10DLC Registration (required for SMS)

US carriers block unregistered A2P SMS. You need to register through 10DLC.

Go to: https://portal.telnyx.com/#/app/messaging/brands

- [ ] **Step 1: Register Brand** — Your business identity
  - Business name, EIN or sole proprietor info
  - Business address, website (ifixyour.app)
  - Vertical: "Technology"
  - ~$4 one-time fee
- [ ] **Step 2: Create Campaign** — What you're sending
  - Use case: "Customer Care" or "Account Notifications"
  - Sample message: "New lead: John (john@example.com) - auth broken, app down"
  - Messaging profile: `ifixyourapp` (already created)
  - ~$15/month
- [ ] **Step 3: Assign number to campaign** — Link +13692108994
- [ ] **Step 4: Wait for approval** — Usually 1-3 business days

Once approved, SMS will flow automatically (worker code is already wired up).

## Cloudflare Custom Domain (optional, nice to have)

- [ ] Add `api.ifixyour.app` custom domain to the worker
  - CF Dashboard → Workers & Pages → ifixyourapp-api → Settings → Domains & Routes → Add Custom Domain
  - Then update fetch URL in index.html from `ifixyourapp-api.winslowcj5.workers.dev` to `api.ifixyour.app`

## Interim: Email Notification

While waiting for 10DLC approval, consider adding email notification as a fallback so you don't miss leads. The D1 database IS capturing all submissions regardless.
