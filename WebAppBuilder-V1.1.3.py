import time
import os
import sys

desktop = os.path.normpath(os.path.expanduser("~/Desktop"))

Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

def fast_type(x):
    for y in x + "\n":
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(0.020)


def end():
   print('\n')
   fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Task successfully ended')
   fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Do you want to do something else?')
   print('\n')
   retry = input(f'{Wh}[ {Gr}? {Wh}] {Gr}y{Wh} to restart / {Gr}n{Wh} to exit: ')
   if retry == 'y':
        main()
   elif retry == 'n':
        exitprogram()
   else:
        error()

def exitprogram():
    fast_type(f'{Wh}[ {Gr}X {Wh}] {Gr}Stopping program{Wh}...')
    exit()

def error():
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Error: Something unexpected happened...')
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Please make sure that you type something correct the next time!')
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Restarting in WebAppBuilder section in 3 seconds...')
    time.sleep(1)
    print(f'{Wh}[ {Gr}+ {Wh}] #')
    time.sleep(1)
    print(f'{Wh}[ {Gr}+ {Wh}] #')
    time.sleep(1)
    print(f'{Wh}[ {Gr}+ {Wh}] #')
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Restarting{Wh}...')
    time.sleep(1)
    main()


def banner():
    os.system('cls')
    print(f"""{Gr}
     __      __ _____                 __________      .__.__       .__
    /  \    /  \  _  \  _____  _____  \______   \__ __|__|  |    __|  |
    \   \/\/   / /_\  \ |  _ \ |  _  \ |    |  _/  |  \  |  |   / __  |
     \        /   |    \|  |_> | |_>  >|    |   \  |  /  |  |__/ /_/  |
      \__/\  / \____|__ |   __/|   __/ |______  /____/|__|____/\____  | 
           \/           |__|   |__|           \/                    \/ 
               {Wh}Electron-based Web app builder --- V1.1.3
    
    <-Coded by TheRedmc-Off->
    """)

def main():
    os.system('cls')
    banner()
    print('\n\n')
    name = input(f'{Wh}[ {Gr}? {Wh}] {Gr}What is the name of the app you want to create{Wh}? ')
    url = input(f'{Wh}[ {Gr}? {Wh}] {Gr}What is the url of the original website{Wh}: ')
    
    os.chdir(desktop)
    os.system(f'nativefier --name "{name}" "{url}"')
    os.system('cls')
    banner()
    print('\n\n')
    fast_type(f'{Wh}[ {Gr}+ {Wh}] {Wh}The Web app has been built in: "{Gr}{desktop}\{name}-win32-x64{Wh}"')
    fast_type(f'{Wh}[ {Gr}+ {Wh}] {Gr}Open the app folder?')
    print('\n\n')
    open = input(f'{Wh}[ {Gr}? {Wh}] {Gr}y{Wh} to open / {Gr}n{Wh} to exit: ')
    if open == 'y':
        os.system(f'explorer.exe "{desktop}\{name}-win32-x64"')
        end()
    elif open == 'n':
        exitprogram()
    else:
        error()


def fatalError():
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Fatal Error')
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Please make sure that you type something correct the next time!')
    fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Stopping program in 3 seconds...')
    time.sleep(1)
    print(f'{Wh}[ {Gr}+ {Wh}] #')
    time.sleep(1)
    print(f'{Wh}[ {Gr}+ {Wh}] #')
    time.sleep(1)
    print(f'{Wh}[ {Gr}+ {Wh}] #')
    time.sleep(1)
    exitprogram()

def installNativefier():
    os.system('cls')
    banner()
    print('\n\n')
    fast_type(f'{Wh}[ {Gr}+ {Wh}] {Gr}Do you want to install or update Nativefier?')
    fast_type(f'{Wh}[ {Gr}+ {Wh}] {Gr}Please note that NPM in required to run this program')
    fast_type(f'{Wh}[ {Gr}+ {Wh}] {Gr}The NPM packages folder {Wh}(node_modules){Gr} needs to be added\n      to PATH for this program to work!')
    print('\n\n')
    install = input(f'{Wh}[ {Gr}? {Wh}] {Gr}y{Wh} to install / {Gr}n{Wh} to exit: ')
    if install == 'y':
        os.system('cls')
        banner()
        print('\n\n')
        fast_type(f'{Wh}[ {Gr}+ {Wh}] Please wait, the {Gr}Nativefier{Wh} installation/update has been started...')
        time.sleep(2)
        os.system('cls')
        os.system(f"npm install nativefier")
        os.system(f"npm audit fix")
        os.system(f"npm fund")
        time.sleep(3)
        os.system('cls')
    elif install == 'n':
        fast_type(f'{Wh}[ {Gr}! {Wh}] {Gr}Nativefier NPM package is required to run this program,\n      and it needs to be up-to-date or installed if needed!')
        time.sleep(3)
        exitprogram()
    else:
        fatalError()


os.system('cls')
installNativefier()
banner()
print('\n\n')
fast_type(f'{Wh}[ {Gr}1 {Wh}] {Gr}Start WebAppBuilder tool')
fast_type(f'{Wh}[ {Gr}0 {Wh}] {Gr}Exit')
print('\n\n')
menu = input(f'{Wh}[ {Gr}+ {Wh}] {Gr}WEBApp@Build~# {Wh}')

if menu == '1':
   main()
elif menu == '0':
   exitprogram()
else:
   error()
