import sys
import socket
import requests
import socks
from colorama import init, Fore, Style
import time


init(autoreset=True)


print("Ultimate Hacker Tool V2.2")
time.sleep(2)
print("Connecting to TOR")
def connect_to_socks():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050, True)
    socket.socket = socks.socksocket
r = requests.get('http://wtfismyip.com/text')
print(Style.BRIGHT + Fore.BLUE + "CURRENT IP:", r.text) #prints my ordinary IP address
print("CONNECTING SOCKS....")
connect_to_socks()
r = requests.get('http://wtfismyip.com/text')
print(Style.BRIGHT + Fore.BLUE + "CURRENT IP:", r.text)


tar = input("Enter target address:    ")
print("Hacking", tar)
time.sleep(1.5)
print("Vulnerability found!!!")
time.sleep(2.2)
print("Extracting Data......")
time.sleep(1)
print("Finishing Attack")
time.sleep(0.5)
print(tar, "HAS BEEN SUCCESSFULLY HACKED!!!")
print(Style.BRIGHT + Fore.RED + "--------------WAITING---------------------")
time.sleep(0.5)
print(Style.BRIGHT + Fore.GREEN + "--------------ACCESS GRANTED--------------")
print("Press 1 to log into root")
print("Press 2 to dump database")
print("press 3 for DOS Attack")
todo = input("Select [1] , [2] , [3]:   ")
if todo == "1":
    print("Logging in...")
    time.sleep(3)
    print("Error......")
    print("QUITTING!!!")
    sys.exit()
elif todo == "2":
    print("Getting Data ready please wait..")
    time.sleep(5)
    print("Error......")
    print("QUITTING!!!")
    sys.exit()
elif todo == "3":
    print("SENDING PACKETS..")
    time.sleep(0.5)
    print("SENDING PACKETS..")
    time.sleep(0.5)
    print("SENDING PACKETS..")
    time.sleep(0.5)
    print("Error......")
    print("QUITTING!!!")
    sys.exit()
else:
    print("INVALID INPUT!!!")
    print("ERROR: QUITTING....")
    sys.exit()
