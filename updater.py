from requests import get
from time import sleep
from functions import *
from variables import *
import tkinter.messagebox
import webbrowser

def check_update():
    """Checks for updates"""
    change_title(f"Real Lopez")
    print(f"    [{red}>{reset}] Procurando atualizações")
    
    try:
        latest_version = get("https://raw.githubusercontent.com/l1pezim1/real_lopez/master/version").text.rstrip()
    except:
        print(f"    [{red}>{reset}] Could not connect to server")
        sleep(2)
        return
    
