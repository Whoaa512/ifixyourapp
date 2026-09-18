#!/bin/bash
set -euo pipefail

PLIST_SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/com.ifixyourapp.leads.plist"
PLIST_DST="$HOME/Library/LaunchAgents/com.ifixyourapp.leads.plist"
UID_N=$(id -u)

launchctl bootout "gui/$UID_N/com.ifixyourapp.leads" 2>/dev/null || true

cp "$PLIST_SRC" "$PLIST_DST"
launchctl bootstrap "gui/$UID_N" "$PLIST_DST"
launchctl enable "gui/$UID_N/com.ifixyourapp.leads"

echo "installed + started com.ifixyourapp.leads"
