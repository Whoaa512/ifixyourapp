#!/usr/bin/env bash
# /// script
# description = "Bulk domain availability checker for brand protection"
# ///
#
# Usage: ./scripts/check-domains.sh
# Checks domain availability via whois lookups.
# Rate-limited to avoid getting blocked by whois servers.

set -euo pipefail

DELAY=2  # seconds between lookups to avoid rate limiting

domains=(
  # Tier 1 — Critical
  "fixyourapp.com"
  "fixyourapp.app"
  "fixyour.app"
  "i-fix-your-app.com"
  "i-fix-your.app"
  "ifixyou.app"
  "wefixyourapp.com"
  "wefixyour.app"

  # Tier 2 — High
  "ifixyourapp.io"
  "ifixyourapp.dev"
  "ifixyourapp.co"
  "ifixyourapp.net"
  "ifixyour.dev"
  "ifixyour.io"
  "ifixyoursoftware.app"
  "vibecoderescue.com"
  "ifixyourapp.ai"

  # Tier 3 — Medium
  "fixmyapp.app"
  "ifxyour.app"
  "ifixyourapp.org"
  "ifixyourapp.tech"
  "ifixyoir.app"
  "i-fix-your-app.app"
  "ifix-your.app"

  # Shortener candidates
  "fixd.app"
  "fxyr.app"
  "ifyx.app"
  "fxya.app"
  "fixa.app"
  "ifix.app"
)

printf "%-30s  %-12s  %s\n" "DOMAIN" "STATUS" "DETAILS"
printf "%-30s  %-12s  %s\n" "------" "------" "-------"

for domain in "${domains[@]}"; do
  result=$(whois "$domain" 2>&1 || true)

  if echo "$result" | grep -qiE "no match|not found|no data found|domain not found|no entries found|available|status: free"; then
    status="AVAILABLE"
    details=""
  elif echo "$result" | grep -qiE "rate limit|quota exceeded|try again later"; then
    status="RATE-LIMITED"
    details="retry later"
  elif echo "$result" | grep -qiE "registrar:|creation date|registered on|domain name:"; then
    registrar=$(echo "$result" | grep -i "registrar:" | head -1 | sed 's/.*Registrar: *//I' | tr -d '\r')
    expiry=$(echo "$result" | grep -iE "expir|paid-till" | head -1 | sed 's/.*: *//' | tr -d '\r')
    status="TAKEN"
    details="${registrar:+Registrar: $registrar}${expiry:+ | Expires: $expiry}"
  else
    status="UNKNOWN"
    details="manual check needed"
  fi

  printf "%-30s  %-12s  %s\n" "$domain" "$status" "$details"
  sleep "$DELAY"
done

echo ""
echo "Done. $(date)"
