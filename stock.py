#!/usr/bin/env python3
import sys
import sqlite3
import os
import datetime
from tabulate import tabulate
from time import sleep
from pathlib import Path

def stocks(con,cursor):
    print("Have you made any trades today(y/n)")
    checker = input()
    counter = 0
    while(checker == 'y'):
        try:
            if(checker == 'y'):
                counter += 1
                print("Name of stock")
                name = input()
                print("Amount invested")
                amount = float(input())
                print("Profit Made")
                profit = float(input())
                returnAmount = float(input("Return Amount\n"))
                numberofstocks = int(input("Number of Stocks\n"))
            else:
                print("Got! it")
        except:
            counter = 0
            print("Amount/Profit/Return/Stocks values might be wrong")
        if(counter >= 1):
            date = str(datetime.date.today())
            cursor.execute("insert into dailytransaction values(?,?,?,?,?,?)",(name,amount,profit,returnAmount,numberofstocks,date))
            conn.commit()
            print("Transaction history updated")
        checker=input("You wish to add more trades(y/n)\n")

def display(conn,cursor): #DisplayMethod
    cursor.execute("select * from dailytransaction")
    result = cursor.fetchall()
    print(tabulate(result,headers=['Name','Amout Invested','Profit','Return Amount','Number Of Stocks','Date'],tablefmt='psql'))
    sleep(20)

if __name__ == "__main__":
    conn = sqlite3.connect('/home/varun/stock/Stock.db')
    cursor = conn.cursor()  #Executer
    stocks(conn,cursor)
    hist = input("View history(y/n)\n")
    if(hist == 'y'):
        display(conn,cursor)
        conn.close()
    else:
        print("Bye!")
        conn.close()
