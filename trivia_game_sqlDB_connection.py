import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset=True)

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-CFNBSI63;'
                      'Database=student;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
def data_entry():
    first = input(Fore.LIGHTMAGENTA_EX + "Enter your first name: ")
    last = input(Fore.LIGHTMAGENTA_EX + "Enter your last name: ")
    age = int(input(Fore.LIGHTMAGENTA_EX + "Enter your age name: "))
    id = int(input(Fore.LIGHTMAGENTA_EX + "Enter your score out of 5: "))
    cursor.execute("INSERT INTO st1 (Fname, Lname, age, id) VALUES(?, ?, ?, ?)",(first, last, age, id))
    conn.commit()