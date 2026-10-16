# Screenshots the home page expects

The home page has two screenshot strips. Each frame shows a real PNG when the
file exists, and a placeholder (a blank screen in the frame with the shot's name on
it) when it does not. Replacing a PNG under the same name needs only a `?v=` bump;
a NEW shot needs its `<figure>` in the strip and a caption key in i18n.js (all 17
languages). A screen reader hears one label per frame: the image's alt, or the
placeholder's title only if the image failed (`shotFailed` in index.html).

Strip shots are **736 × 1600** PNG, portrait (resized from 1206 × 2622 `simctl io …
screenshot` captures of an iPhone 17 Pro simulator). The frame crops to that aspect,
so another size still shows but may be cropped at the top and bottom.

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
| `shot-1.png` | (to come) The Counter: the camera counting dominoes on a real table — FIRST in the strip |
| `shot-2.png` | The scoreboard: Los Tigres 165 · Las Águilas 130, six rounds in the ledger |
| `shot-6.png` | Four players in OLED mode: Juan 65 · Rosa 75 · Miguel 15 · Carmen 20, five rounds showing |
| `shot-3.png` | A tournament bracket: "Sunday Classic", both Round 1 matches FINAL, the Final Round card at the edge |
| `shot-4.png` | Game history: four single games with their winners |
| `shot-5.png` | Settings → Appearance with the 🇩🇴 flag header on: Theme, Header Size, App Color (off while a flag is on), Flag Animation |

In strip order. `shot-5` and `shot-6` were added 2026-10-01 (same simulator and
launch switches, settings restored afterwards: theme System, no flag, tournament
mode back on).

The first three (shot-2/3/4) are RAW simulator screenshots (736 × 1600, from 1206 × 2622 captures on "MD Site
Shots", light mode, `-debugPremium 1 -headerSize_MagicDomino Minimal`), taken
2026-09-30 in the evening so the header is the caps lockup. They replaced the four
App Store marketing images (a phone drawn inside the picture, English captions
baked in, the old mixed-case header) — those sat inside the page's own phone frame
as a phone inside a phone.

⚠️ **`shot-1.png`, the AI camera counting, is the one shot still to come — and its slot
is READY, first in the strip** (Juan, 2026-10-01: the Counter leads "so the counter can
get more spotlight"). The simulator has no camera, so it comes from a real phone: the
Counter tab with dominoes on the table and the count showing, on the Minimal header
tier. **To add it: drop it in as `shot-1.png` (736 × 1600 — resize with `sips -z 1600
736`), bump the `?v=` in every html page, commit, push.** No markup edit: the figure is
already in `#scoreStrip` and removes itself while the file is absent (`shotAbsent` in
index.html), so the live site never shows an empty phone. Its caption (`alt.shot1`)
already exists in all 17 languages.

## The game strip (felt)

| File | Shows |
|---|---|
| `play-shot-1.png` | The table mid-hand: 2 vs 2 (Juan & Rico against Luna & Max), a long snake, four playable tiles lit |
| `play-shot-7.png` | The Play home with the Online card in front: the signal over your pill, Find a match, Play with friends, "Have a code? Join" |
| `play-shot-10.png` | The LOCKED! card the moment a table locks, sparks still flying (2 vs 2, Dominican) |
| `play-shot-6.png` | The hand card after a lock: JUAN & RICO TAKE THE HAND · +14 · The count (Rico locked it, 1 against Max's 5) |
| `play-shot-11.png` | The DOMINÓ! card with Rico's pill as he goes out, the celebration around it (2 vs 2) |
| `play-shot-2.png` | The Play home: the Computer card's seating picture (Rico across, Max and Luna on their nameplates, your pill), Table setup row, Deal, the Computer · Online tabs, the Daily Deal row |
| `play-shot-3.png` | Pick your game: the ten tables, Dominican selected |
| `play-shot-9.png` | The rulebook, How to play, Dominican selected: the Dominican card, The object, Who's on your side |

The table above is in STRIP order (Juan, 2026-10-12, final: table, Online, Locked, hand card, Dominó!, Play the computer, pick your game, how to play); it ends on the rulebook again (the 2026-10-01 "ends on the rulebook" rule is superseded). `play-shot-8` (Capicúa, old score header) is no longer on the page — the Dominó! shot replaced it.
Neither strip has a row of feature or table chips above it any more (removed
2026-10-01: the table picker shot and the premium section already say it). `play-shot-4` (the lobby with its code) was dropped
2026-10-01 by decision — a code on a marketing page is noise. `play-shot-8` was taken
from a deal staged by a TEMPORARY DEBUG switch (deal until the computer, playing every
seat, ends a hand with your capicúa; hand it back one tile short), then removed: a
capicúa is too rare to wait for. The card is up ~1.5 s, so start a background
`simctl io … screenshot` loop BEFORE the tap and pick the settled frame.
All eight are 736 × 1600, resized from 1206 × 2622 `simctl io … screenshot` captures,
recaptured 2026-10-01 on "MD Site Shots" with the status bar overridden to 9:41
(the table and the hand card show none — Play hides it in a game). Launched with
`-debugLaunchTab play -debugPremium 1` so no ad banner shows;
`hasSeenOnboarding` set with `simctl spawn … defaults write`. (Until 2026-10-01 that
launch landed on the scorekeeper's Tournament tab whenever tournament mode was on; the
app now keeps the tab a `-debugLaunchTab` asks for. `-debugPlayHost internet` opens a
lobby once the splash lifts — the quickest way to an online table.)
Replace any of them by dropping a new PNG under the same name.

**2026-10-12:** play-shot-1, -2, -6, -7, `hero-play.png` and `duo-split.png` recaptured for 5.0's Play
(two-card home, the seating picture, Rico as your partner, the Quick Match sheet). The bracket
(`play-shot-5`) left the strip — Play's tournaments are hidden in 5.0. The table frames and the
hand card come from a `recordVideo` of `-debugPlayAutopilot 1` (full-resolution frames picked from
the movie: the hand card's total blurs in, so take a frame ~1 s after it lands). The Duo shot has a
seven-round game written to the container's `roundScores.json` and the team names passed as
`-team1Name_MagicDomino` / `-team2Name_MagicDomino`; fold/unfold with `PlayDebugTools/duo-hub.js`.

## The scoreboard redesign (2026-10-13)

The iOS 26 Score page was redesigned (the app's CLAUDE.md, "THE iOS 26 SCORE PAGE"): the totals
under the names with a race bar and "N to win", the rounds as one card, the TOTAL pill gone. Every
site picture that shows the board was recaptured in all 17 languages, same seeds and launch
settings as `tools/sitecap/cap.py`: `hero-score.png` + `shot-2.png` (Los Tigres 165 · Las Águilas
130), `shot-6.png` (four players, OLED) and `duo-split.png` (the Score half beside a dealt hand).
`social-card.png` re-rendered from the new hero. `SHOT_V` and every `i18n.js?v=` bumped to
20261013a (shot-6 again as 20261013b: four-player totals went 34 → 38pt). Shot on a clone of "MD Site Shots" (so 9:41 and the answered prompts carry over) and the
session's own Duo simulator; the other site pictures were not touched.

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
link is shared: the split hero — the two real phones (`hero-score.png`,
`hero-play.png`) under their headlines, the caps wordmark and magicdomino.com across
the foot. Rendered from `social-card.html` with the same CSS as the hero (the
command is in that file's header; if Chrome's one-shot `--screenshot` hangs on the
web fonts, render it through DevTools instead). Re-render it whenever either hero
phone changes. Checked current 2026-10-01 (a fresh render matched the PNG).

## Every language (2026-10-12)

Juan: "the screenshots should change with the language". Every phone on the home page — both heroes,
the scorekeeper strip, the Play strip and the Duo — is shot in all 17 languages: English at the root,
the others in `shots/<lang>/` under the same file names. `i18n.js` swaps each `img[data-shot]` to its
language's copy for every language in `SHOT_LANGS` (a language left out keeps English; nothing can show
an empty phone). Bump `SHOT_V` in i18n.js when the pictures change.

How they were made (scripts kept in `tools/sitecap/`): `cap.py UDID all LANG…` on two clones of
"MD Site Shots" (iPhone 17 Pro) — each static screen is one launch with DEBUG switches
(`-AppleLanguages`, `-debugLaunchTab`, `-play.deckPage 1|2`, `-debugPlaySheet picker|rules`, seeded
`roundScores.json`/`pastGames.json`/`activeTournament.json`), then two autopilot games recorded as
movies: 2 vs 2 (table, hero, Dominó!) and 1 v 1 with no drawing (most hands lock: Locked! + its hand
card). `pick.py LANG` finds the moments (red plate, gold banner, the last gold card before a hand card,
a still board with no red marks); `overrides.json` holds the two picked by eye (fr, bn Dominó!).
`duo.py LANG…` shoots the opened Duo (`-debugLaunchTab playSplit -debugDuoDemo deal`). `assemble.py`
resizes into the site. The computers wear each language's own names, so the boards differ by language
— that is the point. ~1 h 40 min for all 17 on two simulators.

## The phone frames (2026-10-13)

Juan: "see how thick the bezels of these screenshots are? make them thin like actual device bezel
iphone 18 pro max". Every frame (`.mock`, `.shot-frame`) is sized from its OWN width, `--w`: the
bezel is `--bz` = 1.4% of it (1.1% on the felt, where the dark screen reads as frame), circular
corners at 15% of the width with the screen's corner `15% − bezel` (concentric), and the Dynamic
Island at a real island's proportions on the status bar's line. ⛔️ Never a `%` padding: a padding
percentage resolves against the PARENT's width — the hero's whole pane — which drew a bezel ~5% of
the phone. The social card reuses `.mock`; re-render it after any change here.
The opened Duo (`.duo-frame`) gets the same ~6pt bezel: 0.65% of its 951pt inner screen, corners
6.1% / 8.7% (the screenshot's own 5.5% / 7.9% plus the bezel). Its padding % is safe only because
the figure fills its grid cell — keep it that way.

## The new Play tab icon (2026-10-15)

The Play tab's icon changed from a die to the app's own `play.domino` (a fanned hand of dominoes).
Every phone with a tab bar (hero-score, shot-2…6, play-shot-2, play-shot-7 × 17 languages, 136
files) had the old die swapped IN PLACE, not re-shot: `/tmp/iconpatch/swap.py` finds the die by an
edge-map template match (all hits 0.90–0.94; real dominoes on the felt top out at 0.68), fills it
from its surroundings and draws the new glyph's mask in the die's own ink, at the size the app
draws it (measured on a fresh capture: 69/62 of the die's height, same centre). `play-shot-2` was
then RE-SHOT in all 17 languages anyway: the Computer card changed (Deal above Table setup, the
chosen game's opening on the table). `SHOT_V` 20261015a. social-card and duo-split show no tab bar.
