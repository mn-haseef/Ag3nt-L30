import os
import time
import pyfiglet


# Color codes for console output
BLACK = "\033[0;30m"
DARK_GRAY = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
GRAY = "\033[0;37m"
RESET = "\033[0m"

def run_PE():
    file = input(f"{DARK_GRAY} Enter the path and name of the file : {RESET}")
    os.system("python3 Extract/PE_main.py {}".format(file))

def run_URL():
    os.system('python3 Extract/url_main.py')

def exit():
    os.system('exit')

def start():

    # Print the banner with red color
    print(f"""{GREEN}

        ██     ▄▀  ▄███▄      ▄     ▄▄▄▄▀ █     ▄███▄   ████▄ 
        █ █  ▄▀    █▀   ▀      █ ▀▀▀ █    █     █▀   ▀  █   █ 
        █▄▄█ █ ▀▄  ██▄▄    ██   █    █    █     ██▄▄    █   █ 
        █  █ █   █ █▄   ▄▀ █ █  █   █     ███▄  █▄   ▄▀ ▀████ 
        █  ███  ▀███▀   █  █ █  ▀          ▀ ▀███▀         
        █                █   ██                             
        ▀                                                    {RESET} Version 1.0

    {BLUE}
                Ag3nt-L30 written by: Haseef Ahmed
                github:{RESET} https://github.com/mn-haseef/Ag3nt-L30.git

                {RED}Malware Detector {RESET}
    """)


    print(f'''{GREEN}Options{RESET}''')
    print(" 1. PE scanner")
    print(" 2. URL scanner")
    print(" 3. Exit\n")

    select = int(input(f"{DARK_GRAY}Enter your choice : {RESET}"))

    if (select in [1,2,3]):

        if(select == 1):
            run_PE()
            choice = input("Do you want to search again? (y/n)")
            if(choice not in ['Y','N','n','y']):
                print(f'''{RED}Entered an Incorrect Value{RESET}''')
                time.sleep(3)
                exit()
            else:
                if(choice == 'Y' or 'y'):
                    start()
                elif(choice == 'N' or 'n'):
                    exit()
         
        
        elif(select == 2):
            run_URL()
            choice = input("Do you want to search again? (y/n)")
            if(choice not in ['Y','N','n','y']):
                print(f'''{RED}Entered an Incorrect Value{RESET}''')
                time.sleep(3)
                exit()
            else:
                if(choice == 'Y' or 'y'):
                    start()
                else:
                    exit()

        else:
            exit()
    else:
        print(f'''{RED}Entered an Incorrect Value{RESET}''')
        time.sleep(3)
        exit()

start()
