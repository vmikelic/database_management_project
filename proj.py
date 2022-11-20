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
    print("7. Quit")
    choice = input("Enter a choice (1-7): ")
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
                    display_found = 0
                    for x in myresult:
                        if(display_choice == x[2]):
                            print("Display found:"+" serialNo- '"+x[0]+"' ,"+" schedulerSystem- '"+x[1]+"' ,"+" modelNo- '"+x[2]+"'")
                            display_found = 1
                    if(display_found == 0):
                        print("No display found with specified modelNo.")
                    print("")
                elif(display_choice == 3):
                    displaying = 0
                else:
                    print("")
                    print("Invalid choice.")
                    print("")
        else:
            print("No results found.")
    elif (choice == 2):
        sql = "SELECT * FROM DigitalDisplay;"
        mycursor.execute(sql)
        myresultDD2 = mycursor.fetchall()

        if (len(myresultDD2) > 0):
            displaying = 1

            while (displaying == 1):
                print("1. Search digital displays by scheduler system")
                print("2. Exit to main menu")
                display_choice = input("Enter a choice (1 or 2): ")
                try:
                    display_choice = int(display_choice)
                except:
                    display_choice = 0

                if (display_choice == 1):
                    print("")
                    display_no = 1
                    display_choice = input("Enter the scheduler system (Random, Smart, or Virtue) "
                                           "to search by: ").strip().lower()
                    display_found = 0
                    for x in myresultDD2:
                        display_no = 1
                        if (display_choice == x[1].lower()):
                            print(f'Display {display_no}: serialNo- {x[0]}, schedulerSystem- {x[1]}, modelNo- {x[2]}')
                            display_no += 1
                            display_found = 1
                    if (display_found == 0):
                        print("No display found with specified scheduler system.")
                    print("")
                elif (display_choice == 2):
                    displaying = 0
                else:
                    print("")
                    print("Invalid choice.")
                    print("")
        else:
            print("No results found.")
    elif (choice == 3):

        displaying = 1

        # get selection from user
        while (displaying == 1):
            print("1. Insert a new digital display")
            print("2. Exit to main menu")
            display_choice = input("Enter a choice (1 or 2): ")
            try:
                display_choice = int(display_choice)
            except:
                display_choice = 0

            if (display_choice == 1):

                # get digital display data from user
                modelNo_user = ""
                while(True):
                    modelNo_user = input("Enter model number: ").strip()
                    if(modelNo_user == '?stop#'):
                        break
                    if(len(modelNo_user)>0 and len(modelNo_user)<11):
                        break
                    else:
                        print("")
                        print("Invalid model number. Minimum length: 1,Maximum length: 10")
                        print("Type '?stop#' to exit.")
                        print("")
                if(modelNo_user == '?stop#'):
                    displaying = 0
                    break    

                # get model numbers from db
                sql = "SELECT modelNo FROM Model;"
                mycursor.execute(sql)
                myresultM2 = mycursor.fetchall()

                model_found = 0
                for x in myresultM2:
                    if(modelNo_user == x[0]):
                        model_found = 1

                # update model if model not exist
                if (len(myresultM2) == 0) or model_found == 0:
                    print("")
                    print("Model number not found. Updating model information.")

                    ask_model_info = 1
                    add_model = 1
                    while(ask_model_info == 1):
                        try:
                            while(True):
                                width_user = round(float(input("Enter width: ")), 2)
                                if(width_user > 0):
                                    break
                                else:
                                    print("Invalid width. Must be a positive number.")
                            while(True):
                                height_user = round(float(input("Enter height: ")), 2)
                                if(height_user > 0):
                                    break
                                else:
                                    print("Invalid height. Must be a positive number.")
                            while(True):
                                weight_user = round(float(input("Enter weight: ")), 2)
                                if(weight_user > 0):
                                    break
                                else:
                                    print("Invalid weight. Must be a positive number.")
                            while(True):
                                depth_user = round(float(input("Enter depth: ")), 2)
                                if(depth_user > 0):
                                    break
                                else:
                                    print("Invalid depth. Must be a positive number.")
                            while(True):
                                screensize_user = round(float(input("Enter screen size: ")), 2)
                                if(screensize_user > 0):
                                    break
                                else:
                                    print("Invalid screen size. Must be a positive number.")
                            print("")
                            print("You are about to create a Model with the following attributes:")
                            print("modelNo: "+modelNo_user)
                            print("width: "+str(width_user))
                            print("height: "+str(height_user))
                            print("weight: "+str(weight_user))
                            print("depth: "+str(depth_user))
                            print("screenSize: "+str(screensize_user))

                            while(True):
                                print("")
                                confirm_choice = input("Do you wish to proceed? (Y/N): ")
                                if(confirm_choice.lower()[0] == 'y'):
                                    print("Model added.")
                                    ask_model_info = 0
                                    break
                                if(confirm_choice.lower()[0] == 'n'):
                                    print("Going to main menu.")
                                    ask_model_info = 0
                                    add_model = 0
                                    break
                                else:
                                    print("Invalid choice.")
                        except:
                            print("")
                            print("Invalid data. Enter positive numbers only.")

                    if(add_model == 0):
                        displaying = 0
                        break

                    data = [(modelNo_user, width_user, height_user, weight_user, depth_user, screensize_user)]
                    sql = "insert into Model(modelNo, width, height, weight, depth, screenSize) values (%s, %s, %s, %s, %s, %s);"
                    mycursor.executemany(sql, data)
                    mydb.commit()
                    print("")
                    print("Digital display will use newly created modelNo '"+modelNo_user+"'.")
                    print("")

                serialNo_user = ""
                while(True):
                    serialNo_user = input("Enter serial number: ").strip()
                    if(serialNo_user == '?stop#'):
                        break
                    if(len(serialNo_user)>0 and len(serialNo_user)<11):
                        break
                    else:
                        print("")
                        print("Invalid serial number. Minimum length: 1,Maximum length: 10")
                        print("Type '?stop#' to exit.")
                        print("")
                if(serialNo_user == '?stop#'):
                        displaying = 0
                        break    

                # get model numbers from db
                sql = "SELECT serialNo FROM DigitalDisplay;"
                mycursor.execute(sql)
                myresultM2 = mycursor.fetchall()

                serial_found = 0
                for x in myresultM2:
                    if(serialNo_user == x[0]):
                        serial_found = 1

                if(serial_found == 1):
                        print("DigitalDisplay with this serialNo already exists. Exiting to main menu.")
                        displaying = 0
                        break

                scheduler_user = ""
                while(True):
                    scheduler_user = input("Enter scheduler system (Random, Smart, or Virtue): ").strip()
                    if(scheduler_user == '?stop#'):
                        break
                    if scheduler_user.lower() == 'random':
                        scheduler_user = "Random"
                        break
                    elif scheduler_user.lower() == 'smart':
                        scheduler_user = "Smart"
                        break
                    elif scheduler_user.lower() == 'virtue':
                        scheduler_user = "Virtue"
                        break
                    else:
                        print("")
                        print("Invalid scheduler system. Choose Random, Smart, or Virtue")
                        print("Type '?stop#' to exit.")
                        print("")
                if(scheduler_user == '?stop#'):
                        displaying = 0
                        break

                print("")
                print("You are about to create a DigitalDisplay with the following attributes:")
                print("serialNo: "+serialNo_user)
                print("schedulerSystem: "+scheduler_user)
                print("modelNo: "+modelNo_user)
                
                while(True):
                    print("")
                    confirm_choice = input("Do you wish to proceed? (Y/N): ")
                    if(confirm_choice.lower()[0] == 'y'):
                        print("DigitalDisplay added.")
                        print("")
                        ask_model_info = 0
                        break
                    if(confirm_choice.lower()[0] == 'n'):
                        print("Going to main menu.")
                        ask_model_info = 0
                        add_model = 0
                        break
                    else:
                        print("Invalid choice.")

                data = [(serialNo_user, scheduler_user, modelNo_user)]
                sql = "insert into DigitalDisplay(serialNo, schedulerSystem, modelNo) values (%s, %s, %s);"
                mycursor.executemany(sql, data)
                mydb.commit()

                # Query DigitalDisplay and show results
                sql = "SELECT * FROM DigitalDisplay;"
                mycursor.execute(sql)
                myresultDD3 = mycursor.fetchall()

                display_no = 1

                for x in myresultDD3:
                    print(f'Display {display_no}: serialNo- {x[0]}, schedulerSystem- {x[1]}, modelNo- {x[2]}')
                    display_no += 1

                print("")

            elif (display_choice == 2):
                displaying = 0
            else:
                print("")
                print("Invalid choice.")
                print("")
    elif (choice == 4):
        # get DigitalDisplay data
        sql = "SELECT * FROM DigitalDisplay;"
        mycursor.execute(sql)
        myresultDD4 = mycursor.fetchall()

        if (len(myresultDD4) > 0):

            displaying = 1
            display_no = 1

            # show DigitalDisplay data
            for x in myresultDD4:
                print(f'Display {display_no}: serialNo- {x[0]}, schedulerSystem- {x[1]}, modelNo- {x[2]}')
                display_no += 1
                display_found = 1
            print()

            while (displaying == 1):
                print("1. Delete a digital display")
                print("2. Exit to main menu")

                # get user selection
                display_choice = input("Enter a choice (1 or 2): ")
                try:
                    display_choice = int(display_choice)
                except:
                    display_choice = 0

                if (display_choice == 1):
                    print("")

                    # get serial number to delete
                    delete_choice = input("Enter the 'serialNo' for the Digital Display to delete: ").strip()
                    print()

                    sql ='SELECT serialNo,modelNo from DigitalDisplay;'
                    mycursor.execute(sql)
                    myresultDD5 = mycursor.fetchall()

                    serial_found = 0
                    for x in myresultDD5:
                        if(delete_choice == x[0]):
                            serial_found = 1
                            model_delete = x[1]
                            break

                    if(serial_found == 0):
                            print("DigitalDisplay with this serialNo doesn't exist. Exiting to main menu.")
                            displaying = 0
                            break
                    
                    display_delete = 1
                    print("You are about to delete a DigitalDisplay with serialNo '"+delete_choice+"'")
                    while(True):
                        print("")
                        confirm_choice = input("Do you wish to proceed? (Y/N): ")
                        if(confirm_choice.lower()[0] == 'y'):
                            print("DigitalDisplay deleted.")
                            print("")
                            break
                        if(confirm_choice.lower()[0] == 'n'):
                            print("Going to main menu.")
                            display_delete = 0
                            break
                        else:
                            print("Invalid choice.")

                    if(display_delete == 0):
                        displaying = 0
                        break
                    
                    sql = 'DELETE FROM DigitalDisplay WHERE serialNo like %s;'
                    mycursor.execute(sql, ([delete_choice]))
                    mydb.commit()

                    sql = "(SELECT modelNo from Model)" \
                          "EXCEPT" \
                          "(SELECT m.modelNo from Model as m,DigitalDisplay as d where m.modelNo = d.modelNo GROUP BY m.modelNo);"
                    
                    mycursor.execute(sql)
                    myresultDD6 = mycursor.fetchall()
                    
                    for x in myresultDD6:
                        if(model_delete == x[0]):
                            sql = 'DELETE FROM Model WHERE modelNo like %s;'
                            mycursor.execute(sql, ([model_delete]))
                            mydb.commit()
                            print("No other digital displays use Model with modelNo '"+model_delete+"'. Model deleted.")
                            print("")
                            break
                    
                    print("Displays:")
                    print("")
                    sql = "SELECT * FROM DigitalDisplay;"
                    mycursor.execute(sql)
                    myresultDD4 = mycursor.fetchall()

                    if (len(myresultDD4) > 0):
                        display_no = 1

                        # show DigitalDisplay data
                        for x in myresultDD4:
                            print(f'Display {display_no}: serialNo- {x[0]}, schedulerSystem- {x[1]}, modelNo- {x[2]}')
                            display_no += 1
                        print()
                    else:
                        print("No DigitalDisplays to display.")

                    print("Models:")
                    print("")
                    sql = "SELECT * FROM Model;"
                    mycursor.execute(sql)
                    myresultDD4 = mycursor.fetchall()

                    if (len(myresultDD4) > 0):
                        display_no = 1

                        # show DigitalDisplay data
                        for x in myresultDD4:
                            print(f'Model {display_no}: modelNo- {x[0]}, width- {x[1]}, height- {x[2]}, weight- {x[3]}, depth- {x[4]}, screenSize- {x[5]}')
                            display_no += 1
                        print()
                    else:
                        print("No Models to display.")

                elif (display_choice == 2):
                    displaying = 0
                else:
                    print("")
                    print("Invalid choice.")
                    print("")
        else:
            print("No results found.")
    elif (choice == 5):
        
        sql = "SELECT * FROM DigitalDisplay;"
        mycursor.execute(sql)
        myresultDD7 = mycursor.fetchall()

        if (len(myresultDD7) > 0):

            displaying = 1
            display_no = 1

            # show DigitalDisplay data
            for x in myresultDD7:
                print(f'Display {display_no}: serialNo- {x[0]}, schedulerSystem- {x[1]}, modelNo- {x[2]}')
                display_no += 1
                display_found = 1
            print()

            while (displaying == 1):
                print("1. Update a digital display")
                print("2. Exit to main menu")

                # get user selection
                display_choice = input("Enter a choice (1 or 2): ")
                try:
                    display_choice = int(display_choice)
                except:
                    display_choice = 0

                if (display_choice == 1):
                    print("")

                    # get record to update
                    update_serialNo = input("Enter the 'serialNo' for the Digital Display to update: ").strip()
                    for x in myresultDD7:
                        if x[0] == update_serialNo:
                            print()
                            # get updates to perform
                            print('Enter updates at prompt, if not applicable, leave blank.')
                            update_ss = ""
                            while(True):
                                update_ss = input(f'Enter update (Random, Smart, or Virtue) '
                                     f'to scheduler system for serial number: {update_serialNo}: ').strip()
                                if(update_ss == ''):
                                    break
                                if update_ss.lower() == 'random':
                                    update_ss = "Random"
                                    break
                                elif update_ss.lower() == 'smart':
                                    update_ss = "Smart"
                                    break
                                elif update_ss.lower() == 'virtue':
                                    update_ss = "Virtue"
                                    break
                                else:
                                    print("")
                                    print("Invalid scheduler system. Choose Random, Smart, or Virtue.")
                                    print("Leave blank to not update.")
                                    print("")
                            
                            # get model numbers from db
                            sql = "SELECT modelNo FROM Model;"
                            mycursor.execute(sql)
                            myresultM2 = mycursor.fetchall()

                            update_mdl = ""
                            while(True):
                                update_mdl = input(f'Enter update to model number for serial number: {update_serialNo}: ').strip()
                                if(update_mdl == ''):
                                    break
                                model_found = 0
                                for x in myresultM2:
                                    if(update_mdl == x[0]):
                                        model_found = 1
                                if(model_found == 1):
                                    break
                                else:
                                    print("")
                                    print("Invalid model number.")
                                    print("Leave blank to not update.")
                                    print("")

                            print("")
                            # store update data
                            data_scheduler = [(update_ss, update_serialNo)]
                            data_model = [(update_mdl, update_serialNo)]

                            if (len(update_ss) > 0):
                                sql = "UPDATE DigitalDisplay SET schedulerSystem = %s WHERE serialNo = %s;"
                                mycursor.executemany(sql, data_scheduler)

                            if (len(update_mdl) > 0):
                                sql = "UPDATE DigitalDisplay SET modelNo = %s WHERE serialNo = %s;"
                                mycursor.executemany(sql, data_model)
                            
                            mydb.commit()
                            # get digital display data
                            sql = 'SELECT * FROM DigitalDisplay;'
                            mycursor.execute(sql)
                            myresultDD8 = mycursor.fetchall()

                            display_no = 1
                            
                            # show digital displays
                            for x in myresultDD8:
                                print(f'Display {display_no}: serialNo- {x[0]}, '
                                    f'schedulerSystem- {x[1]}, modelNo- {x[2]}')
                                display_no += 1
                    print()

                elif (display_choice == 2):
                    displaying = 0
                else:
                    print("")
                    print("Invalid choice.")
                    print("")
        else:
            print("No results found.")
    elif(choice == 6):
        ## Close connections
        if mydb.is_connected():
            mydb.close()
            mycursor.close()
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
    elif(choice == 7):
        running = 0
    else:
        print("Invalid choice.")

## Close connections
if mydb.is_connected():
    mydb.close()
    mycursor.close()

