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
