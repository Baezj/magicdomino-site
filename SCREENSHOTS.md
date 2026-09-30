# Screenshots the home page expects

The home page has two screenshot strips. Each frame shows a real PNG when the
file exists and draws its own placeholder (a felt or paper frame with the shot's
subject sketched in) when it does not. Drop the file in with the exact name below,
commit, push — nothing else to change. No markup edit, no resize step.

All shots are **1320 × 2868** (an iPhone 17 Pro screenshot at full resolution),
portrait, PNG. The frame crops to that aspect, so a different size still shows but
may be cropped at the top and bottom.

## The hero phones

`hero-score.png` and `hero-play.png` (736 × 1600) are the two real phones in the
split hero: the scoreboard mid-game (Los Tigres 165 · Las Águilas 130, light
mode, the MINIMAL header tier — `-headerSize_MagicDomino Minimal` at launch, so more
of the board shows in the crop) and the table mid-hand. Captured 2026-09-30 on the "MD Site Shots"
simulator; the scoreboard by naming the teams and adding six rounds by hand, the
table from the same capture as `play-shot-1.png`, unshifted, so the names and
scores stay at the top of the phone. The scoreboard was recaptured the same evening
after the wordmark went to caps (MAGIC · mark · DOMINO™), so the phone on the site
shows the header the app ships. The bezel, glow and entrance are CSS (`.mock` in
site.css); at every width the phone stands straight, centred under its headline.
Drop a new PNG under the same name and bump the `?v=` to replace either.

## The scorekeeper strip (light)

| File | Shows |
|---|---|
| `shot-2.png` | The scoreboard: Los Tigres 165 · Las Águilas 130, six rounds in the ledger |
| `shot-3.png` | A tournament bracket: "Sunday Classic", both Round 1 matches FINAL, the Final Round card at the edge |
| `shot-4.png` | Game history: four single games with their winners |

Three RAW simulator screenshots (736 × 1600, from 1206 × 2622 captures on "MD Site
Shots", light mode, `-debugPremium 1 -headerSize_MagicDomino Minimal`), taken
2026-09-30 in the evening so the header is the caps lockup. They replaced the four
App Store marketing images (a phone drawn inside the picture, English captions
baked in, the old mixed-case header) — those sat inside the page's own phone frame
as a phone inside a phone.

⚠️ **`shot-1.png`, the AI camera counting, is MISSING on purpose.** The simulator has
no camera, so the Counter cannot be photographed there. It wants a screenshot from a
real phone: the Counter tab with dominoes on the table and the count showing, taken
with the app on the Minimal header tier. Drop it in as `shot-1.png` (any iPhone
resolution at the 736 : 1600 aspect), add its `<figure>` back as the first item of
`#scoreStrip` in index.html (copy the scoreboard's, `alt.shot1`), bump the `?v=`.

## The game strip (felt)

| File | Shows |
|---|---|
| `play-shot-1.png` | The table mid-hand: 1 v 1 against Rico, ten tiles down, three playable tiles lit |
| `play-shot-2.png` | The Play home: the three cards, Computer in front, Table setup row, Deal |
| `play-shot-3.png` | Pick your game: the ten tables, Dominican selected |
| `play-shot-4.png` | An Anywhere lobby with its six-letter code, one open seat |
| `play-shot-5.png` | A tournament bracket: Singles · 4, semi-final You vs Vega |
| `play-shot-6.png` | The hand card: RICO TAKES THE HAND · NO SCORE · Race to 200 |

Captured 2026-09-30 on an iPhone 17 Pro simulator (a fresh device named
"MD Site Shots", launched with `-debugLaunchTab play -debugPremium 1` so no ad
banner shows; `hasSeenOnboarding` set with `simctl spawn … defaults write`).
Replace any of them by dropping a new PNG under the same name.

## The Duo

`duo-split.png` (1800 wide) is the opened iPhone Duo's inner screen: the scoreboard
on the left half, a 2 vs 2 hand on the right. Captured with
`-debugLaunchTab playSplit -debugDuoDemo deal -debugPremium 1` on the Duo simulator
and `simctl io <duo> screenshot --display=3 --mask=black`; recaptured 2026-09-30 in
the evening for the caps lockup with the mark between the words. ⚠️ The Duo must be
SIDEWAYS (a 2853 × 2007 capture; 2007 × 2853 means it is upright and the split does
not show) — set it from Device Hub's Device → Orientation → Portrait, which
`osascript` can click (see the app repo's CLAUDE.md, the Duo section). It is the one picture
that shows the whole idea at once, which is why it has its own section.

## The social card

`social-card.png` (1024 × 500) is what iMessage, WhatsApp and X show when the
link is shared. It is now the split picture, rendered from `social-card.html` with
the same CSS as the hero — the command is in that file's header. ⚠️ It still shows
the OLD hero (CSS drawings and the icon on the seam); the home page moved to two real
phones on 2026-09-30 and the card has not followed yet.
