import os
import requests
import socket

def exitt():
    print("[*]exit or No")
    X=input("====>y/N:")
    if X == "y":
        print("\033[0;32mGoodBye")
        exit()
    elif X == "N":
        return first()
    else:
        print("\033[1;35[!]",end="")
        print("\033[0;31mThe commande typed wrong")
        return exitt()
def main():
    clear()
    banner()
    print("\033[1;33mJust Respect the same LHOST and the same LPORT")
    LHOST=input("LHOST:")
    LPORT=int(input("LPORT:"))
    print("\033[1;35m[+].",end="")
    print("\033[0;34mAfter Re-type your LHOST and LPORT you have to type this commande in the new window:",end="")
    print(f"\033[0;31mnc {LHOST} {LPORT}")
    os.system("python server.py")
    exitt()

def clear():
    os.system("clear")
clear()

def banner():
    # Bannière BatRoot sur 10 lignes
    banner = [
    "BBBB   AAAAA  TTTTT  RRRR    OOO  OOO  TTTTT",
    "B   B  A   A    T    R   R  O   O O   O   T  ",
    "BBBB   AAAAA    T    RRRR   O   O O   O   T  ",
    "B   B  A   A    T    R  R   O   O O   O   T  ",
    "BBBB   A   A    T    R   R  OOO  OOO  T    "
    ]

    for line in banner:
        print("\033[0;35m",line)

    print("**********************************************************")
    print("*                                                        *")
    print("*        Created by                                      *")
    print("*                   Xpid3r                               *")
    print("*                                                        *")
    print("**********************************************************")
banner()
def first():
    print("\033[1;35m[*].",end="")
    print("\033[0;34mthis tool used for ctf because can take /etc/shadow using server")
    print("\033[1;35m[*].",end="")
    print("\033[0;34mbut just do it step by step")
    print("\033[1;35m[*].",end="")
    print("\033[0;34mYou have to use sudo for run this code without issues*.*")
    choice = input("For repeat the banner write [banner]:")
    if choice =="banner":
        print("OK")
        clear()
        return main()
    else:
        print("\033[1;35m[!].",end="")
        print("\033[0;31mThe commande writed wrong!")
        print("\033[1;32m***************************************************************************")
        return first()
first()
