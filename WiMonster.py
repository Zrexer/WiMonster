#!/usr/bin/env python3
import subprocess
import sys
import pystyle

banner = """
 __       __)  __     __)                      
(, )  |  /  , (, /|  /|                        
   | /| /       / | / |  _____   _  _/_  _  __ 
   |/ |/  _(_) /  |/  |_(_) / (_/_)_(___(/_/ (_
   /  |     (_/   '                            
                                               
"""

pystyle.Write.Print(banner, pystyle.Colors.blue_to_cyan, 0)
print()
print()
pystyle.Write.Print('-------------------------------', pystyle.Colors.yellow_to_red, 0.009)
print()
pystyle.Write.Print('|', pystyle.Colors.yellow_to_red, 0.009)
pystyle.Write.Print('         WiMonster       ', pystyle.Colors.blue_to_cyan)
pystyle.Write.Print('|', pystyle.Colors.yellow_to_red, 0.009)
print()
pystyle.Write.Print('-------------------------------', pystyle.Colors.yellow_to_red, 0.009)
print()
print()
print()

def usageConsole():
    return f"""
{colors.white}{colors.BackRed}Usage:{colors.white}  python3 wimonster.py --help
"""

def usageHelp():
    pystyle.Write.Print('{:<20} {:<}'.format('Command', 'Usage'), pystyle.Colors.green_to_yellow, 0)
    print()
    pystyle.Write.Print('-----------------------------', pystyle.Colors.green_to_yellow, 0)
    print()
    pystyle.Write.Print('{:<20} {:<}'.format('--help', 'show this message'), pystyle.Colors.purple_to_blue, 0)
    print()
    pystyle.Write.Print('{:<20} {:<}'.format('--netsh-cracker', 'Start Program to Crack the Netsh and Wlan Profiles'), pystyle.Colors.purple_to_blue, 0)
    print()

class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m' 
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'

def netshCracker():
    meta_data = subprocess.getoutput(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data
    data = data.split('\n')

    profiles = []
    
    for i in data:
        if "All User Profile" in i :
            i = i.split(":")
            i = i[1]
            i = i[1:-1]
            profiles.append(i)
            
        
    print("{:<30}| {:<}".format(f"{colors.red}Wi-Fi Name", f"{colors.red}Password"))
    pystyle.Write.Print('----------------------------------------------', pystyle.Colors.green_to_yellow, 0.01)
    print()
        
    for i in profiles:
        try:
            results = subprocess.getoutput(['netsh', 'wlan', 'show', 'profile', i, 'key = clear'])

            results = results.split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            
            try:
                print("{:<30} {:<}".format(i, results[0]))
        
            except IndexError:
                print("{:<30} {:<}".format(i, ""))

        except Exception as E:
            print(E)

if __name__ == '__main__':
    lis = sys.argv 
    
    if len(lis) == 1:
        print(usageConsole())
        
    if "--help" in lis:
        usageHelp()
        
    if "--netsh-cracker" in lis:
        netshCracker()


