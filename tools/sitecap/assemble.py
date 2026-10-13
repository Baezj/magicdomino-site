# assemble.py LANG… — copy each language's captures into the website under the page's file names.
# English replaces the root files; every other language goes to shots/<lang>/.
import sys, os
from PIL import Image

SITE = os.path.expanduser('~/Documents/DO NOT DELETE - MAGIC DOMINO/magicdomino-site/')
MAP = {'score': ['shot-2.png', 'hero-score.png'], 'oled4': ['shot-6.png'], 'tournament': ['shot-3.png'],
       'history': ['shot-4.png'], 'settings': ['shot-5.png'],
       'table': ['play-shot-1.png'], 'online': ['play-shot-7.png'], 'locked': ['play-shot-10.png'], 'hand': ['play-shot-6.png'],
       'domino': ['play-shot-11.png'], 'computer': ['play-shot-2.png'], 'picker': ['play-shot-3.png'], 'rules': ['play-shot-9.png'],
       'hero': ['hero-play.png']}
for lang in sys.argv[1:]:
    src = f'/tmp/sitecap/cap/{lang}/'
    dst = SITE if lang == 'en' else SITE + f'shots/{lang}/'
    os.makedirs(dst, exist_ok=True)
    missing = []
    for k, names in MAP.items():
        p = src + k + '.png'
        if not os.path.exists(p): missing.append(k); continue
        im = Image.open(p).convert('RGB').resize((736, 1600), Image.LANCZOS)
        for n in names: im.save(dst + n, optimize=True)
    duo = src + 'duo.png'
    if os.path.exists(duo):
        Image.open(duo).convert('RGB').resize((1800, 1266), Image.LANCZOS).save(dst + 'duo-split.png', optimize=True)
    else: missing.append('duo')
    print(lang, 'missing:', missing or 'none')
