## calling the required libraries 
from time import asctime ##-  The link : https://docs.python.org/3/library/time.html
from time import sleep

## it will open a file in the directory will be used to users information
def initLoginFile() :
    loginFile = open("loginFile.txt" , "w") 
    loginFile.write("card PIN\n")           
    loginFile.close()
    
    create()

## checkCardNumber function
#
def checkCardNumber(card_number) :
    cn_flag = True
    cn_flag2 = True
    len_flag = True
    while (cn_flag): #while true the program will keep repeating until cn_flag changes to false
        while not card_number.isdigit() : 
            card_number = input("please enter a 4 unique digit card number: ") #if it is not numbers it will ask for numbers only
            
        else:
            if len(card_number) != 4:
                while (len_flag) and (card_number.isdigit()): #if the input is numbers it will check if it is of length 4
                    if (len(card_number) == 4) :
                        len_flag = False
                    else:
                        card_number = input("please enter a 4 unique digit card number: ")

            for i in range(len(card_number)): #the for loop will check for uniqueness
                for j in range(i+1,len(card_number)):
                    if card_number[i]== card_number[j]: #if it is not unique cn_flag2 will be false
                        cn_flag2 = False 
                        break
                        break
                        
        if cn_flag2 == False : #if cn_flag2 is false it will ask again
            card_number = input("please enter a 4 unique digit card number: ")
            cn_flag2 = True
        else:
            break
    
    return card_number

## checkPIN function 
#
def checkPIN(PIN) :
    PIN_flag = True
    PIN_flag2 = True
    len_flag = True
    while (PIN_flag): #while true the program will keep repeating until PIN_flag changes to false
        while not PIN.isdigit() :
            PIN = input("please enter a 4 unique digit PIN: ") #if it is not numbers it will ask for numbers only
            
        else:
            if len(PIN) != 4:
                while (len_flag):
                    if len(PIN)== 4 and (PIN.isdigit() == True): #if the input is numbers it will check if it is of length 4
                        len_flag = False
                    else:
                        PIN = input("please enter a 4 digit unique PIN: ")

            for i in range(len(PIN)): #the for loop will check for uniqueness
                for j in range(i+1,len(PIN)):
                    if PIN[i]==PIN[j]: #if it is not unique PIN_flag2 will be false
                        PIN_flag2 = False
                        break
                        break
                    
        if PIN_flag2 == False : #if PIN_flag2 is false it will ask again
            PIN = input("please enter a 4 digit unique PIN: ")
            PIN_flag2 = True
        else:
            break
    return PIN

## fileOpener function --> this function will open a file and close it with returning the lines as a list
# 
def fileOpener(file) :
    rFile = open(file , "r")
    rFileList = rFile.readlines()
    rFile.close()
    
    return rFileList

## checkFloatNumber function --> this function will check if an object is a floating number or not
## this function also validate an input as integer number 
#
def checkFloatNumber(num) :
    notaFloat = True
    while notaFloat :
        for i in num :
            if ( i >= '0' and i <= '9' ) or i == "." : ## a float is an integer with a dot in the middle
                notaFloat = False
            else :
                notaFloat = True
                break
        
        if notaFloat :
            num = input("Enter a float number or an integer: ")
    num = float(num)
    return num ## return num as a float

## crete function 
#
def create():
    try :
        loginFileList = fileOpener("loginFile.txt") ## if you don't have this file in the directory
    except IOError :                                ## an error will be raised and then will call 
        initLoginFile()                             ## initLoginFile which should creat the folder
    else :
        print()
        existingCard = True
        while existingCard : 
            card_number = checkCardNumber(input("please enter a 4 unique digit card number: "))
        
            for cardLine in loginFileList : 
                fileCardNum = cardLine.split()[0]
                if card_number == fileCardNum :
                    existingCard = True
                    break
                else :
                    existingCard = False
                
            if existingCard :
                print("This card Number already exist. please, try another one:")
            
        # taking the PIN and check it by calling checkPIN fun.
        PIN = checkPIN(input("please enter a 4 digit unique PIN: "))
    
        email = input("Please Enter your kfupm Email : ")
        email_flag = True
        while(email_flag):
            if (email[10:] != "@kfupm.edu.sa"):
                email = input("Please Enter a valid kfupm Email : ")
            else:
                break
            
        ## writing the info to a file ( the login file )
        loginFile = open("loginFile.txt" , "a") ## this file contains just the card number and pin to use it for
        loginFile.write(card_number + " " + PIN + "\n") ## login fin
        loginFile.close()
    
    
        ## writing the info to a file ( the user file )
        userFile = open(card_number + ".txt" , "a")
        userFile.write("Card Number: " + card_number + "\n")
        userFile.write("PIN: " + PIN + "\n")
        userFile.write("Email: " + email + "\n")
        userFile.write("Balance: 0\n") # using this in other functions like withdrew and deposite
        userFile.write("Borrowed Funds: 0\n") # using this for borrowing feature ( extra feature )
        userFile.write("\n")
        userFile.write("=== OPERATIONS:")
        userFile.close()
    
        print()
        print("Loading ...")
        sleep(3)
        login()

# login function 
# 
def login():
    loginFileList = fileOpener("loginFile.txt")
    print()
    notExistingCard = True
    while notExistingCard : ## cheking if the card num has an info or not in the bank system
        inputCardNum = checkCardNumber(input("Please enter your card number to login: "))
        lineCounter = -1 ## will use this to connect the line of the card num with the line of the pin
        for cardLine in loginFileList : 
            fileCardNum = cardLine.split()[0]
            lineCounter += 1 ##  loginFileList[0] , ....
            if inputCardNum == fileCardNum :
                notExistingCard = False
                break
                
        if notExistingCard :
            print("Not Existing card number. please, try again:")
          
        
    notCorrectPin = True
    while notCorrectPin : 
        inputPIN = checkPIN(input("Please enter your PIN to login: "))   
        if inputPIN == loginFileList[lineCounter].split()[1] :
            notCorrectPin = False ## the login process has approved
            
            fileList = fileOpener(inputCardNum + ".txt") ## writing the login process in the info
            fileList.append("\nlogin - Date: " + asctime() )
            wFile = open( inputCardNum + ".txt" , "w")
            for line in fileList :
                wFile.write(line)
            wFile.close()
            
            print()
            print("Loading ...")
            sleep(3)
            menu(inputCardNum)
        else :
            print("The PIN is not correct. please, try again:")

## menu function 
#
def menu(card_num) :
    print()
    print("BANK ACCOUNT PROGRAM       ") # Printing the menu for the user
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print("----------------------------------------------")
    print("1.   Show account information   ")
    print("2.   Change PIN Number  ")
    print("3.   Withdraw amount of Money   ")
    print("4.   Deposit amount of Money   ")
    print("5.   Pay Bills   ")
    print("6.   View last transactions   ")
    print("7.   Terminate a program   ")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print("----------------------------------------------")
    print()
    feature = input("Enter Your feature: ")
    
    validInput = False

    while not validInput :
        if len(feature) > 1 :
            feature = input("Enter an integer from 1 to 7: ")
        else :
            if feature < '8' and feature > '0' :
                validInput = True
            else :
                feature = input("Enter an integer from 1 to 7: ")

    feature = int(feature)
    if feature == 1 :
        print()
        print("Loading ...")
        sleep(3)
        show(card_num)
        
    elif feature == 2 :
        with open(card_num + ".txt", "r") as f:
            lineNumber = 0
            listt = f.read().split('\n')
            real_pin_num = listt[1].strip().split(': ')[1]
            f.close()
        
        print()
        print("Loading ...")
        sleep(3)
        changePINFun(real_pin_num, card_num)

    elif feature == 3 :
        print()
        print("Loading ...")
        sleep(3)
        moneyToWithdraw = checkFloatNumber(input("how much you want to withdraw: "))
        
        withdrawFun(moneyToWithdraw , card_num)
        
    elif feature == 4 :
        print()
        print("Loading ...")
        sleep(3)
        moneyToDeposit = checkFloatNumber(input("how much you want to deposit: "))
            
        depositFun(moneyToDeposit , card_num)
    
    elif feature == 5 :
        print()
        print("Loading ...")
        sleep(3)
        payBillFun(card_num)
        
    elif feature == 6 :
        print()
        print("Loading ...")
        sleep(3)
        viewTransactionsFun(card_num)
        
    elif feature == 7 :
        print()
        print("Loging out ...")
        sleep(3)
        terminateFun(card_num)

## showFunction 
#
def show(cardNum):
    with open(cardNum + ".txt", "r") as f: #open the file named after the login card number
        lineNumber = 0
        listt = f.read().split('\n') #will seperate the file by lines first line is card nuber, second PIN, third e-mail and forth service  
        available_card_num = listt[0].strip().split(': ')[1]
        available_email = listt[2].strip().split(': ')[1]
        available_balance = listt[3].strip().split(': ')[1]
        available_funds = listt[4].strip().split(': ')[1]
        f.close()
        
    print("") #print each valiable assigned by lines above
    print("The Card Number is:",available_card_num)
    print("Your E-mail is:",available_email)
    print("Balance:",available_balance)
    print("Borrowed Funds:",available_funds)
    print("")
    passing = input("Enter anything to go to the menu ")
    print()
    print("Loading ...")
    sleep(3)
    menu(cardNum)

## changePinFunction 
#
def changePINFun(currentPIN, cardNumber):
    print()
    ## Anas Part :
    fileList = fileOpener(cardNumber + ".txt") #open the file that has the information
    loginFileList = fileOpener("loginFile.txt") #open the login file that has all the card and pin numbers
    
    newPin = checkPIN(input("Enter the new PIN number: ")) #ask the user for the new pin and check it's specifications with checkPIN function

    fileList[1] = "PIN: " + str(newPin) + "\n" #write the new PIN in the information file in the second file 
    fileList.append("\nChange pin: %s -" %newPin + " Date: " + asctime() ) #write the transaction in the file
    wFile = open( cardNumber + ".txt" , "w")
    for line in fileList :
        wFile.write(line)
    wFile.close()
    
    ## Hassan Past :
    ## changing the PIN in the Login file
    line = -1 #line counter
    for pinLine in loginFileList : ## specify the line that has the original PIN
        filePinNum = pinLine.split()[1]
        line += 1 
        if currentPIN == filePinNum :
            break
            
    loginFileList[line] = cardNumber + " " + newPin + "\n" ## change the line to get the new info in Login file
    
    wLogin = open("loginFile.txt" , "w")
    for logLine in loginFileList :
        wLogin.write(logLine)
    wLogin.close()
    
    print()
    print("Your PIN has been successfully changed")
    print()
    print("Loading ...")
    sleep(3)
    menu(cardNumber)

## Withdrew Function 
#
def withdrawFun(money, cardNumber) :
    fileList = fileOpener(cardNumber + ".txt") ## reading all the lines by using the fileOpener function
    
    balance = float( fileList[3].split(": ")[1] ) ## taking the amount of balance from the user file
    newBalance = 0
    
    print()
    if balance == 0 :
        print("You're balance is 0.you can either :")
        print("1 - go to the menu")
        print("2 - borrow money feature")
        choice = input("Choice is ")
        
        validInput = False
        while not validInput : ## validate the choice
            if len(choice) > 1 :
                choice = input("Enter 1 or 2 ")
            else :
                if choice == '1' or choice == '2' :
                    validInput = True
                else :
                    choice = input("Enter 1 or 2 ")
        choice = int(choice)
        
        if choice == 1 :
            print()
            print("Loading ...")
            sleep(3)
            menu(cardNumber)
        else:
            print()
            print("Loading ...")
            sleep(3)
            borrowFun(cardNumber)

    else :
        choice = ""
        balance_flag = True   
        while balance_flag: #while balance_flag is true 
            if balance < money: #if the balane from the file is less the money user wants to withdraw it will ask for different amount
                print("Your balance is %.2f , you can eather :" % balance)
                print("1 - try another amount")
                print("2 - borrow money feature")
                choice = input("Choice is ")
                
                validInput = False ## validate the choice
                while not validInput : 
                    if len(choice) > 1 :
                        choice = input("Enter 1 or 2 ")
                    else :
                        if choice == "1" or choice == '2' :
                            validInput = True
                        else :
                            choice = input("Enter 1 or 2 ")            
                
                if choice == "1" :
                    print()
                    money = checkFloatNumber(input("Another amount: "))
                    print()
                else:
                    balance_flag = False
            else :
                balance_flag = False
                    
        if choice == "2" :
            print()
            print("Loading ...")
            sleep(3)
            borrowFun(cardNumber)
        else :
            newBalance = balance - money
            print("Your balance is: "+str(newBalance))
            
    
            fileList[3] = "Balance: " + str(newBalance) + "\n" #updating the balance
            fileList.append("\nWithdraw: %.2f -" %money + " Date: " + asctime() ) ## adding the opperation to the user's file
    
            wFile = open( cardNumber + ".txt" , "w") ## writing back all the info after updating it
            for line in fileList :
                wFile.write(line)
            wFile.close()
    
            print()
            print("Loading ...")
            sleep(3)
            menu(cardNumber) 

## borrowFun ( The extra service ) 
#
def borrowFun(cardNumber) :
    fileList = fileOpener(cardNumber + ".txt")
    print()
    amount = checkFloatNumber(input("Enter the amount of money you want to borrow: "))
    borrowOriginal = float( fileList[4].split(": ")[1] ) ## taking the amount of borrowed funds from the user file
    
    newBorrowed = borrowOriginal + amount
    
    fileList[4] = "Borrowed Funds: %.2f\n" % newBorrowed #updating the borrowed Funds
    fileList.append("\nBorrow: %.2f -" %amount + " Date: " + asctime() ) ## adding the opperation to the user's file
    
    wFile = open( cardNumber + ".txt" , "w") ## writing back all the info after updating it
    for line in fileList :
        wFile.write(line)
    wFile.close()
    
    depositFun(amount , cardNumber)

## deposit function 
#
def depositFun(nMoney, cardNumber) :
    fileList = fileOpener(cardNumber + ".txt") ## reading all the lines by using the fileOpener functio
    
    balance = float( fileList[3].split(": ")[1] ) ## taking the amount of balance from the info
    newBalance = nMoney + balance
    fileList[3] = "Balance: %.2f\n" % newBalance
    fileList.append("\nDeposit: %.2f -" %nMoney + " Date: " + asctime() ) ## adding the opperation to the user's file

    wFile = open( cardNumber + ".txt" , "w") ## writing back all the info after updating it
    for line in fileList :
        wFile.write(line)
    wFile.close()
    
    print("Your balance is: %.2f" % newBalance)
    print()
    print("Loading ...")
    sleep(3)
    menu(cardNumber)

## payBill function 
#
def payBillFun(cardNumber): 
    print()
    
    fileList = fileOpener(cardNumber + ".txt")
    borrowOriginal = float( fileList[4].split(": ")[1] ) ## taking the amount of borrowed funds from the file
    balance = float( fileList[3].split(": ")[1] ) ## taking the amount of balance from the info
    choice = 2 ## if there are no borrowed money the program will automatically goes to pay a bill
    
    if balance == 0 :
        print("You're balance is 0.you can either :")
        print("1 - go to the menu")
        print("2 - borrow money feature")
        choice = input("Choice is ")
        
        validInput = False
        while not validInput : ## validate the choice
            if len(choice) > 1 :
                choice = input("Enter 1 or 2 ")
            else :
                if choice == '1' or choice == '2' :
                    validInput = True
                else :
                    choice = input("Enter 1 or 2 ")
        choice = int(choice)
        
        if choice == 1 :
            print()
            print("Loading ...")
            sleep(3)
            menu(cardNumber)
        else:
            print()
            print("Loading ...")
            sleep(3)
            borrowFun(cardNumber)
    else :
        if borrowOriginal > 0 :
            print("you have borrowed %.2f" % borrowOriginal)
            choice = input("If you want to pay it back write 1, if you want to pay a bill write 2 :")

            validInput = False
            while not validInput : ## validate the choice
                if len(choice) > 1 :
                    choice = input("Enter 1 or 2 ")
                else :
                    if choice == '1' or choice == '2' :
                        validInput = True
                    else :
                        choice = input("Enter 1 or 2 ")
            choice = int(choice)

        if choice == 1 :
            print()
            print("Loading ...")
            sleep(3)
            print()

            amount = checkFloatNumber(input("Enter the amount that you want to pay back: "))

            validAmount = False
            while not validAmount :
                if amount > borrowOriginal or amount > balance :
                    print("Enter less than %.2f and balance = %.2f" % (borrowOriginal , balance))
                    amount = float(checkFloatNumber(input("Enter the amount that you want to pay back: ")))
                else :
                    validAmount = True

            newBalance = balance - amount
            newBorrowed = borrowOriginal - amount

            fileList[3] = "Balance: %.2f\n" % newBalance
            fileList[4] = "Borrowed Funds: %.2f\n" % newBorrowed #updating the borrowed Funds
            fileList.append("\nPay back: %.2f -" %amount + " Date: " + asctime() ) ## adding the opperation to the user's file

            wFile = open( cardNumber + ".txt" , "w") ## writing back all the info after updating it
            for line in fileList :
                wFile.write(line)
            wFile.close()
            print("Your balance is %.2f" % newBalance)
            print("You have successfully pay back %0.2f" % amount)
            print()
            print("Loading ...")
            sleep(3)
            menu(cardNumber)

        elif choice == 2 :
            print()
            bill = input("Enter the name of the bill: ") ## taking all the required input
            billAccount = checkCardNumber(input("Enter the account number of this bill: "))
            billValue = checkFloatNumber(input("Enter the value of this bill: "))

            if balance < billValue: ## checking if the user has enough balance
                print()
                print("This account does not have enough money for paying this bill.")
                print("you can eather :")
                print("1 - go to the menu")
                print("2 - borrow money feature")
                option = input("Choice is ")

                validInput = False
                while not validInput : ## validate the choice
                    if len(option) > 1 :
                        option = input("Enter 1 or 2 ")
                    else :
                        if option == '1' or option == '2' :
                            validInput = True
                        else :
                            option = input("Enter 1 or 2 ")
                option = int(option)

                if option == 1 :
                    print("You can deposit money from the menu ..")
                    print()
                    print("Loading ...")
                    sleep(3)
                    menu(cardNumber)

                if option == 2 :
                    print()
                    print("Loading ...")
                    sleep(3)
                    borrowFun(cardNumber)

            else:
                newBalance = balance - billValue ## deducting the amount of the bill
                print()
                print("Your balance is %.2f" % newBalance)
                fileList[3] = "Balance: %.2f\n" % newBalance
                fileList.append("\n" + "paying a bill: %s. to account: %s. amount: %.2f " % (bill ,billAccount , billValue) + "- Date: " + asctime() )

                wFile = open( cardNumber + ".txt" , "w") ## writing back all the info after updating it
                for line in fileList :
                    wFile.write(line)
                wFile.close()

                print()
                print("Loading ...")
                sleep(3)
                menu(cardNumber)

## viewTransactions function 
#
def viewTransactionsFun(cardNumber):
    fileList = fileOpener(cardNumber + ".txt")
    
    if len(fileList) == 7 : ## the original file length =  8
        print()
        print("=================")
        print("no transactions")
        print("=================")
        print()
    else :
        print()
        print("====================================================================")
        for line in range(7 , len(fileList)) :
            print(str(line - 6) , " - " , fileList[line])
        print("====================================================================")
        print()
    
    passing = input("Enter anything to go to the menu ")
    print()
    print("Loading ...")
    sleep(3)
    menu(cardNumber)

## terminate Function 
#
def terminateFun(cardNumber):
    file = open(cardNumber + ".txt") #open the file 
    
    lines = [line.strip() for line in file] #Store each line in linesa after striping
    
    for line_index in range(len(lines)-1, -1, -1): #will search from below 
        
        if lines[line_index].find('login') != -1: #search for login opperation
            
            lastLogin = line_index #if found break the loop
            break  
    print()
    print("Last operation :")
    for line_index in range(lastLogin, len(lines)): #print everything after
        print(lines[line_index])
    
## main function 
#
def main():
    # print("Please select your feature either L/l for Login or S/s for Signup : ") #ask for eaither signin or login 
    choice = input("Please select your feature either L/l for Login or S/s for Signup : ")
    
    if choice.upper() == "L": #if the input is eaither l or L it will start the login function
        print("\nLoading ...")
        sleep(3)
        login()
    elif choice.upper() == "S": #if the input is eaither s or S it will start the create function
        print("\nLoading ...")
        sleep(3)
        create()
    else:
        wrong_command = True #if nither it will ask again
        while(wrong_command):
            print("You have choosen wrong Choice, please enter L\l or S\s")
            choice = input()
            if choice.upper() == "L" or choice.upper() == "S":
                wrong_command = False
            else:
                wrong_command = True
        if choice.upper() == "L":
            print()
            print("Loading ...")
            sleep(3)
            login()

        elif choice.upper() == "S":
            print()
            print("Loading Login page ...")
            sleep(3)
            create()

main()
