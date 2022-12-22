


import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import pyodbc
import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset=True)


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-CFNBSI63;'
                      'Database=student;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()



class Sport():

    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-CFNBSI63;'
                          'Database=student;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    def sportBrain(self):
        z = cursor.execute("SELECT question, A, B, C, D, answer FROM Modified WHERE Category like 'sport' ")
        score = 0
        for i in z:
            print(Fore.LIGHTYELLOW_EX+i[0])
            print("")
            print(Fore.LIGHTBLUE_EX + i[1])
            print(Fore.LIGHTBLUE_EX +i[2])
            print(Fore.LIGHTBLUE_EX +i[3])
            print(Fore.LIGHTBLUE_EX +i[4])
            print(Fore.LIGHTGREEN_EX+"----------------------------------------")
            answer = input("Choose your answer: ")
            if answer == i[5]:
              print("your answer is correct")
              print(Fore.LIGHTGREEN_EX+"---------------------------------------")
              score = score + 1
            else:
              print("your answer is wrong")
              print(Fore.LIGHTGREEN_EX + "---------------------------------------")
        print(Fore.RED + "YOU HAVE GOT ", Fore.RED + str(score), Fore.RED + "OUT OF 4")
# x = Sport()
# x.sportBrain()


class Geography():
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-CFNBSI63;'
                          'Database=student;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    def geographyBrain(self):
        y = cursor.execute("SELECT question, A, B, C, D, answer FROM Modified WHERE Category like 'geography' ")
        # print(cursor)
        score = 0
        for i in y:
            print(Fore.LIGHTYELLOW_EX + i[0])
            print("")
            print(Fore.LIGHTBLUE_EX + i[1])
            print(Fore.LIGHTBLUE_EX + i[2])
            print(Fore.LIGHTBLUE_EX + i[3])
            print(Fore.LIGHTBLUE_EX + i[4])
            print(Fore.LIGHTGREEN_EX + "----------------------------------------")
            answer = input("Choose your answer: ")
            if answer == i[5]:
                print("your answer is correct")
                print(Fore.LIGHTGREEN_EX + "---------------------------------------")
                score = score + 1
            else:
                print("your answer is wrong")
                print(Fore.LIGHTGREEN_EX + "---------------------------------------")
        print(Fore.RED + "YOU HAVE GOT ", Fore.RED + str(score), Fore.RED + "OUT OF 3")

# y = Geography()
# y.geographyBrain()

class Astronomy():
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=LAPTOP-CFNBSI63;'
                          'Database=student;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    def astronomyBrain(self):
        x = cursor.execute("SELECT question, A, B, C, D, answer FROM Modified WHERE Category like 'astronomy' ")
        # print(cursor)
        score = 0
        for i in x:
            print(Fore.LIGHTYELLOW_EX + i[0])
            print("")
            print(Fore.LIGHTBLUE_EX + i[1])
            print(Fore.LIGHTBLUE_EX + i[2])
            print(Fore.LIGHTBLUE_EX + i[3])
            print(Fore.LIGHTBLUE_EX + i[4])
            print(Fore.LIGHTGREEN_EX + "----------------------------------------")
            answer = input("Choose your answer: ")
            if answer == i[5]:
                print("your answer is correct")
                print(Fore.LIGHTGREEN_EX + "---------------------------------------")
                score = score + 1
            else:
                print("your answer is wrong")
                print(Fore.LIGHTGREEN_EX + "---------------------------------------")
        print(Fore.RED + "YOU HAVE GOT ", Fore.RED + str(score), Fore.RED + "OUT OF 3")

# a = Astronomy()
# a.astronomyBrain()