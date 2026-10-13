# duo.py LANG… — the opened Duo's split (Score beside a dealt 2 vs 2 hand) in each language.
import sys, os, time, json, subprocess
sys.path.insert(0, '/tmp/sitecap')
from cap import LOC, COMMON, TEAMS, TWO, rounds, run, data, launch
U = open('/tmp/sitecap/duo_udid').read().strip()
run('xcrun', 'simctl', 'status_bar', U, 'override', '--time', '9:41', '--batteryState', 'charged', '--batteryLevel', '100', '--wifiBars', '3', '--cellularBars', '4')
for lang in sys.argv[1:]:
    out = f'/tmp/sitecap/cap/{lang}/'; os.makedirs(out, exist_ok=True)
    D = data(U) + '/Documents/'; os.makedirs(D, exist_ok=True)
    json.dump(rounds(TWO), open(D + 'roundScores.json', 'w'))
    L = ['-AppleLanguages', f'({LOC[lang][0]})', '-AppleLocale', LOC[lang][1]] + COMMON
    launch(U, L + TEAMS + ['-theme_MagicDomino', 'Light', '-tournamentModeEnabled_MagicDomino', '0', '-debugLaunchTab', 'playSplit',
                          '-debugDuoDemo', 'deal', '-play.mode', 'partners', '-play.deckPage', '1'])
    time.sleep(20)
    for _ in range(3):
        r = run('xcrun', 'simctl', 'io', U, 'screenshot', '--display=3', '--mask=black', out + 'duo.png', timeout=40)
        if os.path.exists(out + 'duo.png'): break
    print(lang, 'duo done', flush=True)
