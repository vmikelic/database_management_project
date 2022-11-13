#!/usr/bin/env python3
# python version is 3.10
# Course: CS 453502
# Assignment: Project Part 3
# Student: Vinny, Mike, Candace
# Date: 11/12/2022
# Recent Edit: 11/13/2022

import mysql.connector
import sys
from getpass import getpass
from mysql.connector.errors import Error

#connect to database
ask_input = 1
host_valid = 0
database_valid = 0
login_valid = 0
cleared = 0

while(ask_input == 1):
    print("")
    if(cleared == 0):
        print("Type '?clear#' to clear all login credentials.")
    if(host_valid == 0 and cleared == 0):
        hostInput = input("Enter the database host: ")
        host_valid = 1
        if(hostInput == '?clear#'):
            cleared = 1
            continue
    if(database_valid == 0 and cleared == 0):
        databaseInput = input("Enter the database name: ")
        database_valid = 1
        if(databaseInput == '?clear#'):
            cleared = 1
            continue
    if(login_valid == 0 and cleared == 0):
        userInput = input("Enter the username: ")
        if(userInput == '?clear#'):
            cleared = 1
            continue
        passInput = getpass("Enter the password (hidden): ")
        if(passInput == '?clear#'):
            cleared = 1
            continue
        login_valid = 1
    if(cleared == 1):
        host_valid = 0
        database_valid = 0
        login_valid = 0
        cleared = 0
        print("Credentials cleared.")
    else:
        try:
            mydb = mysql.connector.connect(
                host=hostInput,
                user=userInput,
                password=passInput,
                database=databaseInput
            )
            ask_input = 0
        except mysql.connector.Error as err:
            print("")
            if(err.errno == 2005):
                print("Unknown host.")
                host_valid = 0
            elif(err.errno == 1045):
                print("Incorrect login. User does not have access or password was entered incorrectly.")
                login_valid = 0
            elif(err.errno == 1049):
                print("Database does not exist.")
                database_valid = 0
            print("Press CTRL-C to exit.")

    
#create cursor object
try:
    mycursor = mydb.cursor()
except:
    print("Could not create cursor!")
    if mydb.is_connected():
        mydb.close()
    exit()
print("")
print("Successful connection to database.")

running = 1

while(running == 1):
    print("")
    print("1. Display all the digital displays")
    print("2. Search digital displays given a scheduler system")
    print("3. Insert a new digital display")
    print("4. Delete a digital display")
    print("5. Update a digital display")
    print("6. Logout")
    choice = input("Enter a choice (1-6): ")
    print("")

    try:
        choice = int(choice)
    except:
        choice = 0
    
    if(choice == 1):
        sql = "SELECT * FROM DigitalDisplay;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        if(len(myresult) > 0):
            displaying = 1

            while(displaying == 1):
                print("1. List all displays")
                print("2. List display by modelNo")
                print("3. Exit to main menu")
                display_choice = input("Enter a choice (1-3): ")
                try:
                    display_choice = int(display_choice)
                except:
                    display_choice = 0
                
                if(display_choice == 1):
                    print("")
                    display_no = 1
                    for x in myresult:
                        print("Display "+str(display_no)+":"+" serialNo- '"+x[0]+"' ,"+" schedulerSystem- '"+x[1]+"' ,"+" modelNo- '"+x[2]+"'")
                        display_no = display_no + 1
                    print("")
                elif(display_choice == 2):
                    print("")
                    display_choice = input("Enter the modelNo to search for: ")
                    display_string = "No display found with specified modelNo."
                    for x in myresult:
                        if(display_choice == x[2]):
                            display_string = "Display found:"+" serialNo- '"+x[0]+"' ,"+" schedulerSystem- '"+x[1]+"' ,"+" modelNo- '"+x[2]+"'"
                    print(display_string)
                    print("")
                elif(display_choice == 3):
                    displaying = 0
                else:
                    print("")
                    print("Invalid choice.")
                    print("")
        else:
            print("No results found.")
    elif(choice == 2):
        print("Search digital displays given a scheduler system.")
    elif(choice == 3):
        print("Insert a new digital display.")
    elif(choice == 4):
        print("Delete a digital display.")
    elif(choice == 5):
        print("Update a digital display.")
    elif(choice == 6):
        running = 0
        print("Successful logout.")
    else:
        print("Invalid choice.")

print("")
## Close connections
if mydb.is_connected():
    mydb.close()
    mycursor.close()

