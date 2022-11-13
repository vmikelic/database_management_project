#!/usr/bin/env python3
# python version is 3.10
# Course: CS 453502
# Assignment: Project Part 2
# Student: Vinny, Mike, Candace
# Date: 10/8/2022
# Recent Edit: 10/13/2022

import mysql.connector
import sys
from getpass import getpass

hostInput = input("Enter the database host: ")
databaseInput = input("Enter the database name: ")
userInput = input("Enter the username: ")
passInput = getpass("Enter the password (hidden): ")

# overwrite user input to default values to reduce time to run/debug
# delete when finished
hostInput='localhost'
userInput='dbuser'
passInput='Iwilldowell'
databaseInput='cs482502'

#connect to database
try:
    mydb = mysql.connector.connect(
        host=hostInput,
        user=userInput,
        password=passInput,
        database=databaseInput
    )
except Exception as e:
    print("Could not connect to the MySQL Server: " + str(e))
    print("Please check the login credentials and try again")
    exit()
    
#create cursor object
try:
    mycursor = mydb.cursor()
except:
    print("Could not create cursor!")
    if mydb.is_connected():
        mydb.close()
    exit()
print("")
print("Successful connection to database")

running = 1

while(running == 1):
    print("")
    print("1. Display all the digital displays.")
    print("2. Search digital displays given a scheduler system")
    print("3. Insert a new digital display")
    print("4. Delete a digital display")
    print("5. Update a digital display")
    print("6. Logout")
    choice = input("Enter a choice (1-6): ")
    print("")
    if(int(choice) == 1):
        print("Display all the digital displays.")
    elif(int(choice) == 2):
        print("Search digital displays given a scheduler system")
    elif(int(choice) == 3):
        print("Insert a new digital display")
    elif(int(choice) == 4):
        print("Delete a digital display")
    elif(int(choice) == 5):
        print("Update a digital display")
    elif(int(choice) == 6):
        running = 0
        print("Successful logout")
    else:
        print("Invalid choice")

## Close connections
if mydb.is_connected():
    mydb.close()
    mycursor.close()

