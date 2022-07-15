import threading, requests, os, random
from colored import fg, attr
from itertools import cycle
from pystyle import Colors, Colorate
from time import strftime, gmtime




print(f"""
    
┌────────────────────────────────────────────────────────┐
│                                                        │
│  ██╗  ██╗██████╗     ███████╗██╗  ██╗ ██████╗ ██████╗  │
│  ██║ ██╔╝██╔══██╗    ██╔════╝██║  ██║██╔═══██╗██╔══██╗ │
│  █████╔╝ ██║  ██║    ███████╗███████║██║   ██║██████╔╝ │
│  ██╔═██╗ ██║  ██║    ╚════██║██╔══██║██║   ██║██╔═══╝  │
│  ██║  ██╗██████╔╝    ███████║██║  ██║╚██████╔╝██║      │
│  ╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝      │
│                                     Boot Script 2.0    │
└────────────────────────────────────────────────────────┘
""")
#webhook link
web = input("Webhook : ")
#"https://discord.com/api/webhooks/997500868586913915/R2NJcDh7BMq1VjW22fophrQQwTEZ9LeFRTQHlxN4diMNeT6WaTbj_EPg4XnR6QFnYLwn"

#colors
a = fg('#a005ed')
b = attr('reset')

#webhook username
rando=["solar#7777","not solar","Define#0001","not Define","ลูกอีดอก","BY KING","หน้าหนี"]

#webhook message
spam="@everyone https://discord.gg/gn7WMYMZPg"

#webhook avatars
avatars = cycle(["https://media.discordapp.net/attachments/778720320035094550/808181516483166228/ec35695c38b97ea470a3d8761930f5d7.png", "https://preview.redd.it/nx4jf8ry1fy51.gif?format=png8&s=a5d51e9aa6b4776ca94ebe30c9bb7a5aaaa265a6", "https://icon-library.com/images/yellow-discord-icon/yellow-discord-icon-15.jpg"])


x = f'{strftime("[%H:%M:%S]", gmtime())} Sent Webhook {spam}'
yes = f'{strftime("[%H:%M:%S]", gmtime())}'


def solarhook(webhook):
 while True:
            
                solarinfo={
                    'username': random.choice(rando),
                    'content': spam,
                    "avatar_url": next(avatars)
                }
                r = requests.post(webhook, json=solarinfo)
                if "retry_after" in r.text:
                    print(f"{a}{yes}{b} ratelimited sleeping for {a}{r.json()['retry_after']}{b} secs.")
                elif r.status_code == 204:
                    print(Colorate.Horizontal(Colors.rainbow,x))
                else:
                    pass



if __name__ == "__main__":
    os.system('cls & title Ecstacy Webhook Spammer - KING DOM SHOP ')
    logo = """
┌─┐┌─┐┌─┐┌┬┐┌─┐┌─┐┬ ┬
├┤ │  └─┐ │ ├─┤│  └┬┘
└─┘└─┘└─┘ ┴ ┴ ┴└─┘ ┴ 
      """
  
    print(Colorate.Horizontal(Colors.rainbow,logo,3))
  
    while True:
     for i in range(10000):
      threading.Thread(target=solarhook, args=(web,)).start()
