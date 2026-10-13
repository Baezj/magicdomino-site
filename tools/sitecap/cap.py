# cap.py UDID LANG… — every website screenshot for each language, on one iPhone 17 Pro simulator.
# Static screens: one launch each. The game: an autopilot 2 vs 2 recorded as a movie (picked later by pick.py).
import sys, os, time, json, subprocess, uuid, plistlib

APP = '/tmp/mdsite/Build/Products/Debug-iphonesimulator/Magic Domino.app'
B = 'MagicDomino.Magic-Domino'
# site code → (AppleLanguages, AppleLocale)
LOC = {'en': ('en', 'en_US'), 'es': ('es', 'es_DO'), 'fr': ('fr', 'fr_FR'), 'pt': ('pt-BR', 'pt_BR'), 'ar': ('ar', 'ar_AE'),
       'zh': ('zh-Hans', 'zh_CN'), 'nl': ('nl', 'nl_NL'), 'de': ('de', 'de_DE'), 'hi': ('hi', 'hi_IN'), 'bn': ('bn', 'bn_BD'),
       'id': ('id', 'id_ID'), 'ur': ('ur', 'ur_PK'), 'tr': ('tr', 'tr_TR'), 'it': ('it', 'it_IT'), 'ja': ('ja', 'ja_JP'),
       'ko': ('ko', 'ko_KR'), 'ru': ('ru', 'ru_RU')}
TOURNEY = {'en': 'Friday Night Classic', 'es': 'Clásico del Viernes', 'pt': 'Clássico de Sexta', 'fr': 'Classique du Vendredi',
           'de': 'Freitagsklassiker', 'it': 'Classico del Venerdì', 'nl': 'Vrijdagavondklassieker', 'ru': 'Пятничная классика',
           'tr': 'Cuma Akşamı Klasiği', 'id': 'Klasik Jumat Malam', 'zh': '周五之夜经典赛', 'ja': '金曜ナイトクラシック',
           'ko': '금요일 밤 클래식', 'ar': 'كلاسيكو ليلة الجمعة', 'ur': 'جمعہ نائٹ کلاسک', 'hi': 'फ्राइडे नाइट क्लासिक',
           'bn': 'ফ্রাইডে নাইট ক্লাসিক'}

def run(*a, timeout=60):
    try: return subprocess.run(list(a), capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired: return None
def data(U): return run('xcrun', 'simctl', 'get_app_container', U, B, 'data').stdout.strip()
def launch(U, args):
    run('xcrun', 'simctl', 'terminate', U, B); time.sleep(0.8)
    run('xcrun', 'simctl', 'launch', U, B, *args)
def snap(U, path):
    for _ in range(3):
        r = run('xcrun', 'simctl', 'io', U, 'screenshot', path, timeout=40)
        if r is not None and os.path.exists(path): return
        time.sleep(2)

def rounds(rows, t=812948550.0):
    out = []
    for i, s in enumerate(reversed(rows)):
        out.append({"timestamp": t - i * 300, "scores": s, "id": str(uuid.uuid4()).upper(), "isFromLiveActivityQuickPoints": False})
    return out
# R1 … R6: Los Tigres 165 · Las Águilas 130 (the site's English board)
TWO = [[35, 0], [0, 55], [50, 0], [0, 25], [80, 0], [0, 50]]
# R1 … R6: Juan 65 · Rosa 75 · Miguel 15 · Carmen 20
FOUR = [[25, 0, 0, 0], [0, 30, 0, 0], [0, 0, 15, 0], [40, 0, 0, 0], [0, 0, 0, 20], [0, 45, 0, 0]]

def clear_resume(U):
    p = data(U) + '/Library/Preferences/' + B + '.plist'
    try:
        d = plistlib.load(open(p, 'rb'))
        for k in ('play.resume.table.v1', 'play.resume.match.v1', 'play.resume.online.v1'): d.pop(k, None)
        plistlib.dump(d, open(p, 'wb'))
    except Exception: pass

COMMON = ['-hasSeenOnboarding', 'YES', '-debugPremium', '1', '-appLanguageSetting_MagicDomino', 'System',
          '-headerSize_MagicDomino', 'Minimal', '-headerBackground_MagicDomino', 'Off', '-appColor_MagicDomino', 'Blue',
          '-customBackgroundEnabled_MagicDomino', '0', '-play.house', 'dominican', '-play.sounds', 'off',
          '-play.identity.name', 'Juan', '-play.resume.table.v1', '', '-play.resume.match.v1', '']
TEAMS = ['-gameMode_MagicDomino', 'Teams', '-team1Name_MagicDomino', 'Los Tigres', '-team2Name_MagicDomino', 'Las Águilas']

def shots(U, lang, out):
    os.makedirs(out, exist_ok=True)
    L = ['-AppleLanguages', f'({LOC[lang][0]})', '-AppleLocale', LOC[lang][1]] + COMMON
    D = data(U) + '/Documents/'
    def shot(name, args, wait=13):
        launch(U, L + args); time.sleep(wait); snap(U, out + name + '.png')
    t = json.load(open('/tmp/sitecap/activeTournament_src.json')); t['title'] = TOURNEY[lang]
    json.dump(t, open(D + 'activeTournament.json', 'w'))
    import shutil; shutil.copy('/tmp/sitecap/pastGames_src.json', D + 'pastGames.json')
    json.dump(rounds(TWO), open(D + 'roundScores.json', 'w'))
    shot('score', ['-debugLaunchTab', 'score', '-theme_MagicDomino', 'Light', '-tournamentModeEnabled_MagicDomino', '0'] + TEAMS)
    shot('history', ['-debugLaunchTab', 'history', '-theme_MagicDomino', 'Light', '-tournamentModeEnabled_MagicDomino', '0'] + TEAMS)
    shot('settings', ['-debugLaunchTab', 'settings', '-theme_MagicDomino', 'Light', '-tournamentModeEnabled_MagicDomino', '0'] + TEAMS)
    shot('tournament', ['-debugLaunchTab', 'score', '-theme_MagicDomino', 'Light', '-tournamentModeEnabled_MagicDomino', '1'] + TEAMS)
    json.dump(rounds(FOUR), open(D + 'roundScores.json', 'w'))
    shot('oled4', ['-debugLaunchTab', 'score', '-theme_MagicDomino', 'OLED', '-tournamentModeEnabled_MagicDomino', '0',
                   '-gameMode_MagicDomino', 'Four Players', '-player1Name_MagicDomino', 'Juan', '-player2Name_MagicDomino', 'Rosa',
                   '-player3Name_MagicDomino', 'Miguel', '-player4Name_MagicDomino', 'Carmen'])
    json.dump(rounds(TWO), open(D + 'roundScores.json', 'w'))
    P = ['-debugLaunchTab', 'play', '-theme_MagicDomino', 'Light', '-tournamentModeEnabled_MagicDomino', '0', '-play.mode', 'partners']
    clear_resume(U)
    shot('online', P + ['-play.deckPage', '2'], 15)
    shot('computer', P + ['-play.deckPage', '1'], 15)
    shot('picker', P + ['-play.deckPage', '1', '-debugPlaySheet', 'picker'], 16)
    shot('rules', P + ['-play.deckPage', '1', '-debugPlaySheet', 'rules'], 16)
    print(lang, 'static done', flush=True)

def game(U, lang, out, kind='partners', seconds=270):
    L = ['-AppleLanguages', f'({LOC[lang][0]})', '-AppleLocale', LOC[lang][1]] + COMMON
    clear_resume(U)
    mov = out + ('game.mov' if kind == 'partners' else 'lock.mov')
    if os.path.exists(mov): os.remove(mov)
    rules = (['-play.mode', 'partners', '-play.drawsFromBoneyard', '1'] if kind == 'partners'
             else ['-play.mode', 'headsUp', '-play.drawsFromBoneyard', '0'])
    launch(U, L + ['-debugLaunchTab', 'play', '-theme_MagicDomino', 'Light', '-tournamentModeEnabled_MagicDomino', '0',
                   '-play.deckPage', '1', '-play.target', '200', '-play.difficulty', 'medium',
                   '-debugPlaySheet', 'deal', '-debugPlayAutopilot', '1'] + rules)
    time.sleep(4)
    rec = subprocess.Popen(['xcrun', 'simctl', 'io', U, 'recordVideo', '--force', mov],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(seconds)
    rec.send_signal(2); rec.wait(timeout=60)
    run('xcrun', 'simctl', 'terminate', U, B); clear_resume(U)
    print(lang, kind, 'recorded', flush=True)

if __name__ == '__main__':
    U, what = sys.argv[1], sys.argv[2]
    run('xcrun', 'simctl', 'install', U, APP)
    run('xcrun', 'simctl', 'status_bar', U, 'override', '--time', '9:41', '--batteryState', 'charged', '--batteryLevel', '100',
        '--wifiBars', '3', '--cellularBars', '4')
    for lang in sys.argv[3:]:
        out = f'/tmp/sitecap/cap/{lang}/'
        os.makedirs(out, exist_ok=True)
        if what in ('static', 'all'): shots(U, lang, out)
        if what == 'partners':
            game(U, lang, out, 'partners', 300)
        if what in ('game', 'all'):
            game(U, lang, out, 'partners', 270)
            game(U, lang, out, 'headsUp', 170)
