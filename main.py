import colorama
import requests
import sys
import os
from colorama import init, Fore
import threading

colorama.init(autoreset=True)

print(Fore.BLUE + """

  $$\                                $$$$$$\                                                    
  $$ |                              $$  __$$\                                                   
$$$$$$\    $$$$$$\   $$$$$$\        $$ /  \__|$$\   $$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\  
\_$$  _|  $$  __$$\ $$  __$$\       $$$$\     $$ |  $$ |\____$$  |\____$$  |$$  __$$\ $$  __$$\ 
  $$ |    $$ /  $$ |$$ |  \__|      $$  _|    $$ |  $$ |  $$$$ _/   $$$$ _/ $$$$$$$$ |$$ |  \__|
  $$ |$$\ $$ |  $$ |$$ |            $$ |      $$ |  $$ | $$  _/    $$  _/   $$   ____|$$ |      
  \$$$$  |\$$$$$$  |$$ |            $$ |      \$$$$$$  |$$$$$$$$\ $$$$$$$$\ \$$$$$$$\ $$ |      
   \____/  \______/ \__|            \__|       \______/ \________|\________| \_______|\__|      
                                                                                 @VENOM_STUDENT
                                                                                 @shivaay
""")

url = "https://check.torproject.org/api/ip"
session = requests.session()
session.proxies = {"http": "socks5h://localhost:9050", "https": "socks5h://localhost:9050"}

response = session.get(url).json()
if response["IsTor"]:
    print("[INFO] Your new IP: " + Fore.LIGHTBLUE_EX + response["IP"])
else:
    print(Fore.RED + "[WARN]" + "Not able to connect to TOR. Make sure TOR is running!")
    sys.exit(0)
target = input(Fore.MAGENTA + "[+]ENTER YOUR TARGET: ")


try:
    response = session.get(target)
    print(Fore.YELLOW + "[INFO] Target is running")
except requests.exceptions.ConnectionError as e:
    print(Fore.RED + "[WARN] Target is seem down")
    sys.exit(0)
print("\n")

wordlist = input(Fore.BLUE + "[+] Enter wordlist path(Press Enter for default): ")
wordlist_path = ""

if wordlist == "":
    print(Fore.YELLOW + "[INFO] Continue with default one...")
    wordlist_path += "sukuna.txt"
else:
    if os.path.exists(wordlist):
        print(Fore.MAGENTA + "[INFO] Wordlist found...\n")
        wordlist_path += wordlist
    else:
        print(Fore.RED + "[WARN] Wordlist not found! Try again please")
        sys.exit(0)

def brutforce():
    print(Fore.YELLOW + "[INFO] Start threading...")
    for i in open(wordlist_path, 'r', encoding="latin9").readline():
        endpoint = i.replace("\n", "")
        finalUrl = ""
        if endpoint.endswith("/"):
            url = target + endpoint
            finalUrl += url
        else:
            url = target + "/" + endpoint
            finalUrl += url
        response = session.get(url).status_code
        if response == 404:
            pass
        else:
            print(Fore.CYAN + f"[FOUND] {finalUrl} [{str(response)}]")


t1 = threading.Thread(target=brutforce(), args=())

t1.start()
t1.join()


