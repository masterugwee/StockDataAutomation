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
    try:
        if(checker == 'y'):
            counter += 1
            print("Name of stock")
            name = input()
            print("Amount invested")
            amount = float(input())
            print("Profit Made")
            profit = float(input())
        else:
            print("Got! it")
    except:
        counter = 0
        print("The amount or profit might be wrong")
    if(counter == 1):
        date = str(datetime.date.today())
        cursor.execute("insert into dailytransaction values(?,?,?,?)",(name,amount,profit,date))
        conn.commit()
        print("Transaction history updated")
        #conn.close()

def display(conn,cursor):
    cursor.execute("select * from dailytransaction")
    result = cursor.fetchall()
    print(tabulate(result,headers=['Name','Amout Invested','Profit','Date'],tablefmt='psql'))
    sleep(20)


if __name__ == "__main__":
        conn = sqlite3.connect('/home/varun/stock/Stock.db')
        cursor = conn.cursor()  #Executer
        stocks(conn,cursor)
        print("View history?(y/n)")
        hist = input()
        if(hist == 'y'):
            display(conn,cursor)
            conn.close()
        else:
            print("Bye!")
            conn.close()
