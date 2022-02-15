
# MANNOJ A/L SAKTHIVEL
# TP060500


import datetime


def register():
    # FUNCTION TO REGISTER USERS
    while True:
        # WHILE TRUE NO NEED TO RECURSIVE
        username = input("Please enter your username: ")
        # INPUT USERNAME
        if 25 >= len(username) >= 7:
        # IF USERNAME IS BETWEEN 7 TO 25 CHARACTERS
            pass # DELETE LINE
        else:
            print("Please enter a username between 7 to 25 characters")
            continue
            # SAME AS REGISTER() (SKIP EVERYTHING FROM LINE 21 AND COME BACK TO LINE 13)

        password = input("Please enter your password: ")
        # INPUT PASSWORD
        if 25 >= len(password) >= 7:
            # IF PASSWORD IS BETWEEN 7 TO 25 CHARACTERS
            pass # DELETE LINE
        else:
            print("Please enter a password between 7 to 25 characters")
            continue
            # CONTINUE UNTIL LAST CONDITION

        email = input("Please enter your email: ")
        # INPUT EMAIL
        if '@' in email and '.com' in  email:
            # IF EMAIL IS CONTAINS '@' AND '.COM'
            pass # DELETE LINE
        else:
            print("Please enter a valid email")
            continue

        hp_no = input("Please enter your phone number: ")
        # INPUT PHONE NUMBER
        if len(hp_no) == 10 or len(hp_no) == 11 and int(hp_no):
        # IF PHONE NUMBER HAS 10 OR 11 INTEGERS
            pass
            break
            #END LOOP
        else:
            print("Please enter a valid malaysian phone number")
            # NO NEED TO CONTINUE AS NOTHING NEEDS TO BE LOOPED AFTER THIS LINE
        # ENDIF
    # END WHILELOOP

    file = open("accountfile.txt", "r")
    # OPEN FILE IN READ MODE
    file.readline()
    # READ LINES IN FILE
    for line in file:

        login_info = line.strip("\n").split(", ")
        # SPLIT ON (", ") AND STRIP THE EXTRA LINE CREATED BY THE FOR LOOP

        if username == login_info[0]:
            # IF USERNAME FOUND IN 0 INDEX OF FILE
            print("username taken")
            condition = True
            # IF USERNAME IN DATABASE, RETURN TRUE
            break
            #TO END LOOP SO ONLY USERNAME IS THE SAME
        elif password == login_info[1]:
            # IF PASSWORD FOUND IN 1 INDEX OF FILE
            print("password taken")
            condition = True
            # IF PASSWORD IN DATABASE, RETURN TRUE
            break
            #TO END LOOP SO ONLY PASSWORD IS THE SAME
        elif email == login_info[2]:
            # IF EMAIL FOUND IN 2 INDEX OF FILE
            print("email taken")
            condition = True
            # IF EMAIL IN DATABASE, RETURN TRUE
            break
            #TO END LOOP SO ONLY EMAIL IS THE SAME
        elif hp_no == login_info[3]:
            # IF HANDPHONE NUMBER IN 3 INDEX OF FILE
            print("phone number taken")
            condition = True
            # IF HANDPHONE NUMBER IN DATABASE, RETURN TRUE
            break
            #TO END LOOP SO ONLY PHONE NUMBER IS THE SAME
        else:
            condition = False
            # IF USERNAME NOT IN DATABASE, RETURN FALSE

        # END LOOP
    # END FOR

    if condition == True:
        print("similarity of details. Please write a different detail based on the line above")
        # PRINT WHEN CONDITION IS TRUE
        register()  # CALL REGISTER FUNCTION

    else:  # IF CONDITION IS NOT TRUE
        file = open("accountfile.txt", "a")  # OPEN TXT FILE
        file.write(username)
        file.write(", ")
        file.write(password)
        file.write(", ")
        file.write(email)                   # WRITE THE NEW USERNAME, PASSWORD, EMAIL AND HAND PHONE NUMBER CREATED TO THE DATABASE.
        file.write(", ")
        file.write(str(hp_no))
        file.write("\n")
        file.close()
        print("Registration successful. Please continue to log in.")


def personal_details():  # MANNOJ A/L SAKTHIVEL
    file = open("accountfile.txt", "r")
    # OPEN FILE
    existing = input("Enter your old details: ")
    # INPUT USERNAME
    new = input("Enter your new details: ")
    # INPUT NEW USERNAME

    data = [] # CREATE A LIST
    for line in file:
        if existing in line:
            # IF INPUTTED DATA FOUND
            newline = line.replace(existing, new)
            # REPLACE OLD DETAILS WITH NEW DETAILS
            data.append(newline)
            # ADD THE NEW NAME INSIDE THE EMPTY LIST
            print("\nDetails successfully changed!\n")

        else: # IF INPUTTED NAME NOT FOUND
            data.append(line) # NO NAMED CHANGED

        # ENDIF
    file.close()
    # CLOSE FILE

    f = open("accountfile.txt", "w")  # open file
    for count in data:
        f.write(count)
        # WRITING BACK THE NEW DATA OR THE UNCHANGED DATA INTO THE FILE
    f.close()
    # CLOSE FILE


def modify_details():
    print("\nWhat would you like to change?\n")
    print("Enter 1 to change password\nEnter 2 to change email address")
    print("Enter 3 to change phone number\n")
    response = input("Enter a response: ")
    if response == "1":
        personal_details()  # IF RESPONSE IS 1, CALL PERSONAL_DETAILS FUNCTION
    elif response == "2":
        personal_details()  # IF RESPONSE IS 2, CALL PERSONAL_DETAILS FUNCTION
    elif response == "3":
        personal_details()  # IF RESPONSE IS 3, CALL PERSONAL_DETAILS FUNCTION
    else:
        print("Enter a valid response.")
        modify_details()
        # PRINT IF OTHER RESPONSES ARE ENTERED

    loginmenu()


def rentcar():
    file = open("cardetails.txt", "r")
    # OPEN FILE
    car_list = file.read()
    file.close()
    # CLOSE FILE
    print(car_list)
    # DISPLAY CARDETAILS.TXT
    print("Would you like to rent a car?\n")
    print("Press y for yes\nPress n for no")
    status = input("Enter a response: ")
    if status == "y":
        # INPUTTED RESPONSE OF USER
        car = input("Please enter full car name as shown in list: ")
        # INPUT FULL NAME OF CAR
        for file in open("cardetails.txt"):
            file = file.strip("\n").split(", ")
            # STRIP EXTRA LINE AND SPLIT IT BY (", ")
            while car in file:
                # IF CAR THAT IS INPUTTED IS IN FILE
                # print(file)
                    user = input("Please enter username: ") #
                # WRITE USERNAME
                    print("Please enter renting duration (DD/MM/YYYY)")
                    start_day = int(input("Start Date: "))
                    start_month = int(input("Start Month: "))               # INPUT STARTING TIME OF RENTING THE CAR
                    start_year = int(input("Start Year: "))
                    start_date = datetime.date(start_year, start_month, start_day)
                    # USING DATETIME MODULE
                    print("Start rent date is ", start_date)
                    #PRINT DATETIME MODULE

                    end_day = int(input("Return Date: "))
                    end_month = int(input("Return Month: "))                           # INPUT WHEN THE USER WISHED TO RETURN THE CAR
                    end_year = int(input("Return Year: "))
                    end_date = datetime.date(end_year, end_month, end_day) # USING DATETIME MODULE
                    print("Return rent date is ", end_date)
                    # PRINT DATETIME MODULE
                    for file in open("rentedCar.txt"):
                        file = file.strip("\n").split(", ")
                        if car in file and str(start_date) == file[2] or str(end_date) == file[3]:
                            # IF CAR, START DATE AND END DATE OF THE CAR THAT WISHED TO BE RENT IS THE SAME AS THE CAR THAT IS CURRENTLY BEING RENTED
                            print("Car is currently rented on that day")
                            # CAR IS UNAVAILABLE
                            condition = True
                            # IF CAR, START DATE OR END DATE IS THE SAME
                            break
                        else:
                            condition = False
                            # IF CAR, START DATE OR END DATE IS NOT THE SAME
                    if condition == False:
                        delta = end_date - start_date
                        print("Duration of tenure is ", delta)
                        print("\nDeposit is MYR500")
                        # DEPOSIT OF MYR500
                        print("Please state your payment method")

                        print("Enter 1 for payment through debit card/credit card\nEnter 2 to pay via touch and go E-wallet")
                        print("Enter 3 for payment through shopee pay\n")
                        # SELECT PAYMENT METHOD
                        answer = input("Please enter a response: ")
                        # INPUTTED ANSWER
                        if answer == "1":
                            debitcard = input("Please enter your debit card/credit card number: ")
                            varification_code = input("Please enter your varification number(back of your card): ")
                            if len(debitcard) == 16 and len(varification_code) == 3 and int(debitcard) and int(varification_code):
                                condition = False
                            else:
                                print("invalid credit card details")
                                condition = True
                        elif answer == "2":
                            print("Please scan the QR code")
                            print("QR code scanned successfully")
                            condition = False
                        elif answer == "3":
                            print("Please scan the QR code")
                            print("QR code scanned successfully")
                            condition = False
                        else:
                            print("Please enter a valid input")
                            condition = True

                    if condition == False:
                    # FOR ALL IF STATEMENTS THAT END WITH CONDITION IS FALSE
                        file = open("rentedCar.txt", "a")
                        file.write(user)
                        file.write(", ")
                        file.write(car)
                        file.write(", ")
                        file.write(str(start_date))                                         # WRITE DETAILS OF THE INPUTTED DATA INTO THE FILE
                        file.write(", ")
                        file.write(str(end_date))
                        file.write(", ")
                        file.write(str(delta))
                        file.write(", ")
                        file.write("payed RM500 deposit")
                        file.write("\n")
                        file.close()
                        print("Payment successful.\nYou will be redirected to menu.")
                        loginmenu()
                        # CALL LOGINMENU FUNCTION
                    else:
                        rentcar()
                        # CALL RENTCAR FUNCTION

        print("Invalid car.")
        # IF CAR IS NOT ON THE DISPLAYED FILE
        rentcar()
        # CALL RENTCAR FUNCTION
    elif status == "n":
        print("You will be redirected to main menu.")
        loginmenu()
        # CALL LOGINMENU FUNCTION
    else:
        print("Please enter a valid response")
        rentcar()
        # CALL RENTCAR FUNCTION


def loginmenu():
    # MENU FUNCTION FOR REGISTERED USERS
    print("Enter 1 to modify personal details\nEnter 2 to view rental history")
    print("Enter 3 to view car details/rent car\nEnter 4 to log out\nEnter 5 to return to main menu\n")
    # SELECT INPUT
    response = input("Please enter a response: ")

    if response == "1":
        # MODIFY PERSONAL DETAILS
        modify_details()

    elif response == "2":
        # VIEW PERSONAL RENTAL HISTORY
        temp_user = input("Please enter username to confirm:")
        file = open("rentedCar.txt", "r")
        file = file.readlines()
        for line in file:
            line = line.strip("\n").split(", ")
            # STRIP("\n") AND SPLIT LINE
            while temp_user in line:
                # SEARCH FOR USER IN LINE
                print(line)
                # PRINT ALL DETAILS OF THE USER ACCORDING TO THE ROWS
                break
                #IF NOT INFINITE LOOP
        print("\nYou will be redirected to main menu\n")
        loginmenu()
        #CALL LOGINMENU FUNCTION

    elif response == "3":
        # RENT CAR
        rentcar()
        #CALL RENTCAR FUNCTION

    elif response == "4":
        # LOG OUT
        print("You are logged out. Thank you for using our service.")

    elif response == "5":
        # RETURN TO MAIN MENU
        main()
        # CALL MAIN MENU FUNCTION

    else:
        print("Please a valid response")
        # IF OTHER RESPONSES ARE ADDED
        loginmenu()
        # CALL LOGINMENU FUNCTION


def login():  # MANNOJ A/L SAKTHIVEL
    # FUNCTION TO LOG IN FOR REGISTERED USERS
    username = input("Please enter your username: ")
    # INPUT USERNAME
    temp_user = username
    password = input("Please enter your password: ")
    # INPUT PASSWORD
    for line in open("accountfile.txt", "r").readlines():
        # READ THE LINES IN THE TEXT FILE
        login_info = line.strip("\n").split(", ")
        # SPLIT ON (", "), AND STORE THE RESULTS IN A LIST OF TWO STRINGS
        if username == login_info[0] and password == login_info[1]:
            # TO VALIDATE USERNAME AND PASSWORD IN THE DATABASE
            print("\nYou are logged in! What would you like to do?\n")
            loginmenu()
            # CALL LOGIN MENU FUNCTION
            return True

    print("Incorrect credentials. Please try again.\n")
    # WHEN USERNAME AND PASSWORD IS INCORRECT
    login()
    # CALL LOGINMENU FUNCTION


# -----------------------------END OF REGISTERED CUSTOMER FUNCTIONS------------------------------


# -----------------------------ADMIN FUNCTIONS (OO CHOONG SOU TP060728)------------------------------


def add_car():  # add_car function
    while True:
        car_name = input("Please enter car name: ")
        # INPUT CAR NAME
        car_engine = input("Please enter engine capacity: ").upper()
        # INPUT CAR ENGINE CAPACITY
        car_segment = input("Please enter car segment: ").upper()
        # INPUT CAR SEGMENT
        car_type = input("Please enter car type: ").capitalize()
        # INPUT CAR TYPE (SEDAN/SUV/HATCHBACK/ETC)

        with open("cardetails.txt", "a") as file:
            # OPEN CAR FILE
            file.write(car_name)
            file.write(", ")
            file.write(car_engine)
            file.write(", ")
            file.write(car_segment)  # APPEND DETAILS TO FILE
            file.write(", ")
            file.write(car_type)
            file.write("\n")

            print(car_name, "has been added.")

        print("\nWould you like to add another car?")
        status = input("Press y to add another car\nPress n to return to menu\n").rstrip()
        # CHECK ADMIN INPUT
        if status == "y":
            continue
            # RE-RUN LOOP

        if status == "n":
            print("You will be redirected to main menu.")
            adminmenu()
            return False
            # TO BREAK/STOP LOOP

        else:
            print("Error, You will be directed to main menu")
            adminmenu()
            # RETURN TO ADMIN MENU
            return False
            # TO BREAK/STOP LOOP
        # END IF
    # END WHILE


def modify():  # FUNCTION TO MODIFY CAR DETAILS
    while True:
        with open("cardetails.txt", "r") as file:
            # OPEN TEXT FILE
            modify_list = file.readlines()
            # READ FROM FILE

        search = input("Please enter keyword to search: ")
        # USER INPUT
        for file in open("cardetails.txt"):
            # OPEN TXT FILE
            if search.upper() in file.upper():
                # ENSURE SEARCH IS IN FILE
                condition = True
                # TRUE IF IN FILE
            else:
                condition = False
                # FALSE IF NOT IN FILE
            # END IF

        if condition == True:
            # IF TRUE
            existing = input("Enter exact existing details: ")
            # USER INPUT
            new = input("Enter new details: ")
            if existing in file:
                # CHECK IF EXISTING IN FILE
                oldline = file
                # USE oldline AS PLACEHOLDER FOR file
                newline = file.replace(existing, new)
                # REPLACE EXISTING WITH NEW IN LIST

                modify_list.remove(oldline)
                # REMOVE EXISTING FROM TEMP LIST
                modify_list.append(newline)
                # APPEND NEW TO TEMP LIST

                with open("cardetails.txt", "w") as file:
                    # OPEN TEXT FILE
                    file.writelines(modify_list)
                    # WRITE CONTENT OF LIST TO FILE

                print("Details has been changed successfully")
                print("You will be redirected to main menu.")
                # DISPLAY THIS WHEN SUCCESSFUL
                adminmenu()
                return False
                # TO BREAK/STOP LOOP
            else:
                print("Invalid details")
                # INVALID DETAILS IF EXISTING NOT IN FILE
                continue
                # RE-RUN LOOP
            # END IF
        else:
            print("Car not found")
            # CAR NOT FOUND IF CONDITION IS FALSE
            continue
            # RE-RUN LOOP
        # END IF
    # END WHILE


def returncar():  # FUNCTION TO RETURN CAR
    while True:
        username = input("Please enter username: ")
        # INPUT USERNAME
        car = input("Please enter rented car name: ")
        # INPUT CAR
        start_date = input("Please enter start of rent (YYYY-MM-DD): ")
        # INPUT START OF RENT
        end_date = input("Please enter end of rent (YYYY-MM-DD): ")
        # INPUT END OF RENT
        carlist = ["Username, Car Model, Start of Tenure, End of Tenure, Duration(Days), Payment Status"]

        for line in open("rentedCar.txt", "r"):
            # OPEN TXT FILE USING FOR LOOP
            line = line.split(", ")
            # SPLIT LINES BY (", ")
            while username == line[0] and car == line[1] and start_date == line[2] and end_date == line[3]:
                # CHECK FOR THESE CRITERIA IN THE FILE
                if "payed RM500 deposit" in line[6]:
                    # CHECK IF "payed RM500 deposit" IN FILE
                    print(carlist)
                    print(line)
                    # DISPLAY LINE
                    payment_amount = int(input("\nPlease enter duration: "))
                    # INPUT PAYMENT_AMOUNT
                    payment_checking = str(payment_amount) + " days"
                    if payment_checking == line[4]:
                        # CHECK IF DURATION IN LINE
                        price = 70 * payment_amount
                        print("\nRM", price, "is to be paid.")
                        payment_due = int(input("\nPlease enter correct amount: "))
                        # INPUT PAYMENT AMOUNT
                        if payment_due == price:
                            # CHECK IF PAYMENT AMOUNT IS EQUAL TO PRICE
                            with open("rentedCar.txt", "r") as file:
                                # OPEN TXT FILE
                                car_file = file.readlines()
                                # READ TXT FILE AS CAR_FILE

                            existing = "payed RM500 deposit"
                            new = ("RM" + str(price) + " payed")
                            # DISPLAY AMOUNT PAYED

                            for file in open("rentedCar.txt"):
                                # OPEN TXT FILE AS FILE
                                if username == line[0] and car == line[1] and start_date == line[2] in file:
                                    # CHECK USERNAME, CAR, AND START_DATE IN FILE
                                    oldline = file
                                    newline = file.replace(existing, str(new))
                                    car_file.remove(oldline)
                                    car_file.append(newline)
                                    with open("rentedCar.txt", "w") as carfile:
                                        # OPEN TXT FILE
                                        carfile.writelines(car_file)
                                        # WRITE CAR_FILE INTO TXT FILE

                                    print("\nCar is returned, payment received.")
                                    return False
                                    # TO BREAK/STOP LOOP
                                # END IF
                            # END FOR
                        else:
                            print("Please enter correct amount.")
                            continue
                            # RE-RUN LOOP
                        # END IF
                    else:
                        print("Please enter correct duration.")
                        continue
                        # RE-RUN LOOP
                    # END IF
                else:
                    print("Payment is done.")
                    return False
                    # END IF
                adminmenu()
            # END WHILE
        # END FOR
    # END WHILE


def display_record():
    while True:
        print("\nPress 1 to view Cars Rented Out")
        print("Press 2 to view car available to rent")
        print("Press 3 to view all customer bookings")
        print("Press 4 to view specified customer bookings")
        print("Press 5 to view customer bookings for a specific time duration")
        print("Press 6 to return to main menu\n")
        choice = input("Please enter response: ").strip()
        # CHECK FOR ADMIN INPUT

        if choice == "1":
            # IF "1" IS CHOSEN
            print("------------Cars currently rented------------")
            for file in open("rentedCar.txt"):
                # OPEN TXT FILE AS FILE
                if "payed RM500 deposit" in file:
                    # CHECK IF "payed RM500 deposit" IN FILE
                    file = file.strip("\n")
                    # STRIP NEW LINE FROM FILE
                    print(file)
                    # DISPLAY FILE
                # END IF
            continue
            # RE-RUN LOOP

        elif choice == "2":
            # IF "2" IS CHOSEN
            print("------------Cars available for rent------------")
            viewcar()
            continue
            # RE-RUN LOOP

        elif choice == "3":
            # IF "3" IS CHOSEN
            print("------------All customer bookings------------")
            for line in open("rentedCar.txt"):
                # OPEN TXT FILE AS LINE
                line = line.strip("\n")
                # STRIP NEW LINE FROM LINE
                print(line)
                # DISPLAY LINE
            continue
            # RE-RUN LOOP

        elif choice == "4":
            # IF "4" IS CHOSEN
            print("------------Search specific record------------")
            details = input("Please enter specific detail to search: ")
            for line in open("rentedCar.txt"):
                # OPEN TXT FILE AS LINE
                line = line.strip("\n")
                # STRIP NEW LINE FROM LINE
                if details in line:
                    # CHECK IF DETAILS IS IN LINE
                    print(line)
                    # DISPLAY LINE
                # END IF
            continue
            # RE-RUN LOOP

        elif choice == "5":
            # IF "5" IS CHOSEN
            search = input("Please enter year and month (YYYY-MM) to search: ")
            for file in open("rentedCar.txt"):
                # OPEN TXT FILE AS FILE
                file = file.split(", ")
                # STRIP NEW LINE FROM FILE
                if search in file[2]:
                    # CHECK IF SEARCH IS IN FILE
                    print(file)
                    # DISPLAY FILE
            continue
            # RE-RUN LOOP

        elif choice == "6":
            # IF "6" IS CHOSEN
            print("You will be redirected to main menu")
            adminmenu()
            break
            # BREAK LOOP

        else:
            # IF ANYTHING BESIDES 1-6 IS INPUTTED
            print("Error, You will be redirected to main menu")
            adminmenu()
            break
            # BREAK LOOP
        # ENDIF
    # END WHILE


def adminmenu():  # FUNCTION FOR MENU FOR ADMINS
    while True:
        print("\n1 Cars\n2 Details\n0 Log Out\n")
        status = input("Enter a response: ").strip()
        if status == "1":
            # IF 1 (CARS) CHOSEN
            print("\nPress a to add car\nPress v to view cars\nPress m to modify contents")
            print("Press r to return car\nPress t to return to main menu\nPress 0 to log out\n")
            status = input("Enter a response: ").strip()
            if status == "a":  # IN (1) CARS MENU
                # TO ADD CAR
                add_car()
                break
                # BREAK LOOP

            elif status == "v":  # IN (1) CARS MENU
                # to view car
                detail_list = ['Car ID, Car Name, Engine Capacity']  # CREATE LIST AS TITLE
                print(detail_list)
                with open("cardetails.txt", "r") as file:
                    # open txt file
                    file = file.read()
                    # READ FROM FILE
                    print(file)
                    # DISPLAY FILE
                    print("You will be redirected back to main menu")
                    continue
                    # RE-RUN LOOP

            elif status == "m":  # IN (1) CARS MENU
                # TO MODIFY CAR DETAILS
                with open("cardetails.txt", "r") as file:
                    # OPEN TXT FILE
                    car_details = file.read()
                    # READ LINE FROM FILE
                    print(car_details)
                    # DISPLAY LINE
                    modify()
                    break
                # BREAK LOOP

            elif status == "r":  # IN (1) CARS MENU
                # TO RETURN CAR
                returncar()

            elif status == "t":  # IN (1) CARS MENU
                # TO RETURN TO MAIN ADMIN MENU
                continue
                # RE-RUN LOOP

            else:
                # IF INVALID RESPONSE IS INPUTTED
                print("Please enter a valid response")
                continue
                # RE-RUN LOOP
            # ENDIF

        elif status == "2":
            # 2 (DETAILS) TO VIEW CAR DETAILS
            display_record()
            break
            # BREAK LOOP

        elif status == "0":
            # TO LOG OUT
            print("You have logged out. Thank you for using our service.")
            break
            # BREAK LOOP
        else:
            # IF INVALID RESPONSE INPUTTED
            print("Please enter a valid response.")
            continue
            # RE-RUN LOOP
    # ENDIF


def adminlogin():
    # function to login for admin user
    while True:
        username = input("Please enter your username: ")
        # input username
        password = input("Please enter your password: ")
        # input password
        for line in open("adminfile.txt", "r").readlines():
            # Read the lines in the txt file
            login_info = line.strip("\n").split(", ")
            # Split on the space, and store the results in a list of two strings
            if username == login_info[0] and password == login_info[1]:
                # to validate username and password in database.
                print("\nYou are logged in! What would you like to do?")
                adminmenu()
                return False
                # TO BREAK/STOP LOOP

        print("Wrong credentials.")
        # IF USERNAME AND/OR PASSWORD DO NOT MATCH
        # WILL CONTINUE LOOP


# -----END OF ADMIN FUNCTIONS-----

def viewcar():  # FUNCTION TO VIEW CAR
    detail_list = ['Car ID, Car Name, Engine Capacity']
    # CREATE LIST AS detail_list
    print(detail_list)
    # DISPLAY LIST
    for line in open("cardetails.txt", "r"):
        # OPEN FILE AS LINE
        line = line.strip("\n")
        # STRIP "NEW LINE" FROM LINE
        print(line)
        # DISPLAY LINE
    # END FOR


# ------------------------------------------MAIN FUNCTION------------------------------------------
def main():  # OO CHOONG SOU TP060728 & MANNOJ A/L SAKTHIVEL TP060500
    while True:
        print("-------------SUPER CAR RENTAL SERVICES---------------")
        print("What would you like to do?\n")
        print("0 View Cars\n1 Login/Register\n2 Quit\n")
        status = input("Please enter a response: ").strip()
        # CHECK USER INPUT

        if status == "0":  # IN MAIN MENU
            # 0 TO VIEW CAR
            viewcar()
            # CALL FUNCTION TO VIEW CARS
            print("\nWould you like to rent a car?\n")
            print("Press y for yes\nPress n for no\n")
            response = input("Please enter a response: ").strip()
            # CHECK USER INPUT
            if response == "y":
                print("\nTo rent a car, please login.\n")
                continue
                # RE-RUN LOOP
            elif response == "n":
                print("You will be redirected to main menu.\n")
                continue
                # RE-RUN LOOP
            else:
                print("Please enter a valid response.")
                continue
                # RE-RUN LOOP
            # END IF

        elif status == "1":  # IN MAIN MENU
            # 1 TO LOGIN/REGISTER
            print("\nWould you like to login or register?\n")
            print("Press 1 to login\nPress 2 to register\nPress 3 to login as admin\n")
            status = input("Please enter a response: ").strip()
            if status == "1":  # IN LOGIN/REGISTER MENU
                # TO LOGIN AS REGISTERED CUSTOMER
                login()
                # LOGIN FUNCTION
                return False
                # TO BREAK/STOP LOOP

            elif status == "2":  # IN LOGIN/REGISTER MENU
                register()
                # TO REGISTER CUSTOMER
                print("Do you want to login now? y for yes/n for no")
                status = input("Please enter response: ")
                # CHECK FOR USER INPUT
                if status == "y":
                    # IF YES, THEN LOGIN
                    login()
                    # CALL LOGIN FUNCTION
                    return False
                    # TO BREAK/STOP LOOP
                elif status == "n":
                    # IF NO, RETURN TO MENU
                    continue
                    # RE-RUN LOOP
                else:
                    # IF INVALID RESPONSE INPUTTED
                    print("Please enter a valid input")
                    print("You will be redirected to the main page")
                    continue
                    # RE-RUN LOOP
                # END IF

            elif status == "3":  # IN LOGIN/REGISTER MENU
                # TO LOGIN AS ADMIN
                adminlogin()
                # CALL ADMIN LOGIN FUNCTION

            else:  # IN LOGIN/REGISTER MENU
                # IF INVALID RESPONSE INPUTTED
                print("Please enter a valid response")
                continue
                # RE-RUN LOOP
            # ENDIF

        elif status == "2":  # IN MAIN MENU
            # TO QUIT
            print("Thank you for using our service. Good-bye.")
            return False
            # TO STOP LOOP

        else:
            # IF INVALID RESPONSE IS INPUTTED
            print("Please enter a valid response.")
            continue
            # RE-RUN LOOP
        # ENDIF


main()  # CALL MAIN FUNCTION


# -------------------------------------END OF MAIN FUNCTION-------------------------------------
