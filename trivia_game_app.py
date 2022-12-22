import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset=True)
from trivia_game_utiles import *
from trivia_game_sqlDB_connection import data_entry

while True:
    print(Fore.YELLOW + "****************************")
    print(Fore.BLUE +'WELCOME TO THIS TRIVIA GAME:')
    print(Fore.YELLOW + "****************************")
    site = input(Fore.LIGHTMAGENTA_EX + """
                    Enter "S" for Sport
                    Enter "G" for Geography
                    Enter "A" for QA Astronomy
                    """)
    print(Fore.RED + "---------------------------------------------------------")
    if site == 's':
         run_sport = Sport()
         run_sport.sportBrain()
    elif site == "g":
         run_geography = Geography()
         run_geography.geographyBrain()
    elif site == "a":
        run_astronomy = Astronomy()
        run_astronomy.astronomyBrain()
    print(Fore.GREEN+"--------------------------------------")
    data_entry()
    print(Fore.GREEN + "--------------------------------------")
    stop = input("do you want to continue? ")
    if stop == "no":
        exit()