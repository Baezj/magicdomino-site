# pick.py LANG — find the moments in cap/LANG/game.mov (2 vs 2) and lock.mov (1 v 1, no drawing) and pull
# them at full resolution: table.png + hero.png (clean boards), domino.png (the DOMINÓ! card, never a
# capicúa), locked.png (the LOCKED! plate, sparks out), hand.png (the hand card after the lock, settled).
import sys, os, glob, json, subprocess
from PIL import Image

lang = sys.argv[1]
base = f'/tmp/sitecap/cap/{lang}/'
STEP = 0.25

def stats(path):
    im = Image.open(path).convert('RGB'); w, h = im.size; px = im.load()
    d = dict(red=0, redtop=0, redlow=0, band=0, mid=0, crown=0, white=0)
    for y in range(int(h * 0.08), int(h * 0.97), 2):
        for x in range(0, w, 2):
            r, g, b = px[x, y]
            if r > 170 and g < 90 and b < 90:
                d['redtop' if y <= h * 0.2 else ('red' if y < h * 0.8 else 'redlow')] += 1
            if y > h * 0.2 and r > 235 and g > 235 and b > 225: d['white'] += 1
    for y in range(int(h * 0.14), int(h * 0.38), 2):          # the hand card's gold banner (lower at 2 vs 2)
        for x in range(int(w * 0.1), int(w * 0.9), 2):
            r, g, b = px[x, y]
            if r > 200 and 140 < g < 215 and b < 120: d['band'] += 1
    for y in range(int(h * 0.40), int(h * 0.56), 2):          # big gold words mid-screen
        for x in range(int(w * 0.1), int(w * 0.9), 2):
            r, g, b = px[x, y]
            if r > 215 and 160 < g < 235 and b < 170: d['mid'] += 1
    for y in range(int(h * 0.30), int(h * 0.44), 1):          # a capicúa's crown over its word
        for x in range(int(w * 0.38), int(w * 0.62), 1):
            r, g, b = px[x, y]
            if r > 215 and 150 < g < 225 and b < 120: d['crown'] += 1
    return d

def analyse(mov, tag):
    fr = base + 'fr_' + tag + '/'
    if not os.path.isdir(fr) or not os.listdir(fr):
        os.makedirs(fr, exist_ok=True)
        subprocess.run(['/tmp/sitecap/fxall', mov, fr, str(STEP), '200'], capture_output=True)
    return [(int(os.path.basename(f)[:-4]) / 1000, stats(f)) for f in sorted(glob.glob(fr + '*.png'))]

def runs(S, cond, minlen=2):
    out, cur = [], []
    for t, s in S:
        if cond(s): cur.append(t)
        elif cur:
            if len(cur) >= minlen: out.append((cur[0], cur[-1]))
            cur = []
    if len(cur) >= minlen: out.append((cur[0], cur[-1]))
    return out

def clean(s): return s['red'] == 0 and s['redtop'] == 0 and s['redlow'] == 0 and s['band'] < 50 and s['mid'] < 30

picks = {}
G = analyse(base + 'game.mov', 'g')
glocks = runs(G, lambda s: s['red'] > 120)
ghands = runs(G, lambda s: s['band'] > 400, 3)
from PIL import ImageChops, ImageStat
frg = base + 'fr_g/'
def still(t):
    # nothing moving: the frame and the ones 0.25 s and 0.5 s later are nearly the same picture
    try:
        a = Image.open(frg + '%07d.png' % round(t * 1000)).convert('L')
        for dt in (0.25, 0.5):
            b = Image.open(frg + '%07d.png' % round((t + dt) * 1000)).convert('L')
            if ImageStat.Stat(ImageChops.difference(a, b)).mean[0] > 0.6: return False
        return True
    except Exception: return False
cands = [(t, s) for t, s in G if t > 15 and clean(s) and still(t)]
if cands:
    best = max(cands, key=lambda p: p[1]['white']); picks['table'] = ('game.mov', best[0])
    far = [p for p in cands if abs(p[0] - best[0]) > 12]
    if far: picks['hero'] = ('game.mov', max(far, key=lambda p: p[1]['white'])[0])
for h in ghands:
    if any(h[0] - 6 < l[0] < h[0] for l in glocks): continue
    win = [(t, s) for t, s in G if h[0] - 4.5 < t < h[0] - 0.5 and s['band'] < 50]
    # the LAST card before the hand summary (a knock's card can come just before it), 0.75 s after it
    # lands — named (its pill fades in at 0.45 s) and not yet leaving
    up = [p for p in win if p[1]['mid'] > 60 and p[1]['crown'] < 40]
    if up:
        run_start = up[-1][0]
        for p in reversed(up[:-1]):
            if run_start - p[0] <= 0.3: run_start = p[0]
            else: break
        picks['domino'] = ('game.mov', min(run_start + 0.75, up[-1][0] - 0.1)); break

if os.path.exists(base + 'lock.mov'):
    K = analyse(base + 'lock.mov', 'k')
    klocks = runs(K, lambda s: s['red'] > 120)
    khands = runs(K, lambda s: s['band'] > 400, 3)
    if klocks:
        l0 = klocks[0][0]; picks['locked'] = ('lock.mov', l0 + 0.3)
        after = [h for h in khands if h[0] > l0]
        if after: picks['hand'] = ('lock.mov', min(after[0][0] + 1.6, after[0][1] - 0.2))
if 'locked' not in picks and glocks:
    l0 = glocks[0][0]; picks['locked'] = ('game.mov', l0 + 0.3)
    after = [h for h in ghands if h[0] > l0]
    if after: picks['hand'] = ('game.mov', min(after[0][0] + 1.6, after[0][1] - 0.2))
if 'hand' not in picks and ghands:
    picks['hand'] = ('game.mov', min(ghands[0][0] + 1.6, ghands[0][1] - 0.2))

# hand-checked picks win (overrides.json: {lang: {name: [movie, seconds]}})
try:
    for name, (m, t) in json.load(open('/tmp/sitecap/overrides.json')).get(lang, {}).items(): picks[name] = (m, t)
except FileNotFoundError: pass
for name, (m, t) in picks.items():
    subprocess.run(['/tmp/fxat', base + m, base + name + '.png', str(t)], capture_output=True)
json.dump({k: [m, t] for k, (m, t) in picks.items()}, open(base + 'moments.json', 'w'))
missing = [k for k in ('table', 'hero', 'domino', 'locked', 'hand') if k not in picks]
print(lang, {k: round(t, 1) for k, (m, t) in picks.items()}, 'MISSING' if missing else '', missing, flush=True)
