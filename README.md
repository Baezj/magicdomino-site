# Magic Domino™ — magicdomino.com

The marketing site for Magic Domino: the dominoes scorekeeper and, since
2026-09-30, the dominoes game — "two rooms, one app". GitHub Pages serves this
folder as-is on every push to `main`; there is no build step.

## How the site is built

- `index.html` — the split home. `support.html`, `privacy.html`, `terms.html` — the
  secondary pages. `404.html` — the not-found page, which also probes a room code.
- `site.css` — ONE stylesheet for every page. Two worlds: `.world-score` (light,
  the brand blue) and `.world-play` (Play's felt, brass and ivory). Tokens are
  re-set inside `.world-play`, so the same components render in either world.
- `i18n.js` — every string in all 17 languages, one line per key. Markup ships
  English with `data-i18n` keys; read the header of that file before adding a word.
  New copy uses the app's own renderings of game terms (see the glossary note there).
- The home page is: the split hero (two real phones), the one line with the store
  badges, the scorekeeper's screenshots, the game's screenshots, the Duo, Premium,
  footer. The six-card feature grids, the "best of both worlds" bridge and the
  Watch-live code box were removed on 2026-09-30 (Juan: "clean up useless things …
  only keep the screenshots sections, the Duo's section, and the paywall section");
  the TV board's own page at /tv/ is the way to enter a code now (nav "Watch Live").
  Their i18n keys are still in i18n.js, unused — harmless, and a removal there is a
  17-language edit for nothing.
- `SCREENSHOTS.md` — which PNGs the home page shows, how each was captured on the
  simulator, and how to replace one. `social-card.html` renders `social-card.png`.
- ⚠️ Every asset reference carries `?v=…`. Cloudflare caches whatever it first
  serves under a URL for four hours, so a probe that beats a Pages build pins a
  404 — or, worse, the OLD file under the NEW version string (2026-09-30, twice).
  Bump the value when an asset changes (`grep -o '?v=[a-z0-9]*' index.html | sort
  -u`), and **do not request a versioned URL until the Pages build for that commit
  reports `built`** (`gh api repos/Baezj/magicdomino-site/pages/builds/latest`,
  matching the commit, not just the status — "latest" is the previous build until
  the new one starts). If a version string is pinned stale, bump it again.
- The old domain, magicdominoapp.com, redirects here permanently from Cloudflare.
  See the app repo's CLAUDE.md, section "TWO DOMAINS", before touching either.

---

# Magic Domino: AI Scorekeeper™ (original notes)

The ultimate AI-powered domino scorekeeper for iOS.

## 🎯 Features
- 🤖 **AI-Powered Counting** - Instantly count domino pips with your camera
- 🏆 **Tournament Mode** - Run professional tournaments with brackets
- 📊 **Score Tracking** - Keep detailed game history
- 🎨 **Beautiful Themes** - Customize your experience
- ☁️ **iCloud Sync** - Access your games across all devices

## 📱 Download

[Download on the App Store] (https://apps.apple.com/us/app/magic-domino-ai-scorekeeper/id6747228055?uo=4)

## 🆘 Support

Need help? Email us at: [magicdominoapp@gmail.com](mailto:magicdominoapp@gmail.com)

---

© 2025 Magic Domino. All rights reserved.

## Android App Links — `/.well-known/assetlinks.json` (prepared 2026-10-23, NOT live yet)

The Android app (`com.magicdomino.android`, 2.0+) verifies `/j/*` (Play invites and Live Share)
and `/d/*` (Daily Deal) on **magicdomino.com, www.magicdomino.com, magicdominoapp.com and
www.magicdominoapp.com**. Android refuses a redirected file, so each host must answer the path
itself with a 200 and `application/json`:

| Host | Who serves `/.well-known/assetlinks.json` |
|---|---|
| magicdomino.com | GitHub Pages, straight from **this repo's `.well-known/assetlinks.json`** (`.nojekyll` lets the dot-folder through) |
| www.magicdomino.com | the relay Worker (route in the relay's `wrangler.toml`), proxying this repo's file from raw.githubusercontent.com |
| magicdominoapp.com, www.magicdominoapp.com | the relay Worker, same proxy — **and** the path must be excluded from the old zone's Single Redirect rule (dashboard), like the AASA and app-ads.txt |

⛔️ **The file does not exist yet on purpose**: it needs the SHA-256 of the **Play App Signing key**
(Play Console → Test and release → App integrity → App signing), which only the Play Console shows.
A made-up fingerprint would make Android mark the links as failed. To turn it on:

1. Copy `tools/assetlinks/assetlinks.template.json` to `.well-known/assetlinks.json`, put the real
   fingerprint(s) in (format `AB:CD:…`, 32 colon-separated pairs, uppercase), and check it parses:
   `python3 -m json.tool .well-known/assetlinks.json`.
2. Commit and push (Pages publishes it on magicdomino.com).
3. Deploy the relay (`wrangler deploy` in magic-domino-relay — the proxy is committed there, fff5e5f)
   between hands, and add `/.well-known/assetlinks.json` to the exclusions of magicdominoapp.com's
   redirect rule.
4. Check every host answers 200 JSON with no redirect:
   `for h in magicdomino.com www.magicdomino.com magicdominoapp.com www.magicdominoapp.com; do curl -s -o /dev/null -w "$h %{http_code} %{content_type}\n" https://$h/.well-known/assetlinks.json; done`
   and Google's checker: `https://digitalassetlinks.googleapis.com/v1/statements:list?source.web.site=https://magicdomino.com&relation=delegate_permission/common.handle_all_urls`.
5. On a phone: `adb shell pm verify-app-links --re-verify com.magicdomino.android`, then
   `adb shell pm get-app-links com.magicdomino.android` → every host `verified`.

⚠️ `.well-known/apple-app-site-association` here is NOT what iPhones read: the relay Worker serves the
AASA on both apexes (its routes win over Pages). Leave this repo's copy alone.
