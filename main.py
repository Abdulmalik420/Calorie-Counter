import os
import datetime
import csv
import pandas as pd
from tabulate import tabulate

x = datetime.datetime.now()
nowDate = x.strftime("%d")
nowMonth = x.strftime("%B")
mainPath = os.getcwd()

def newUserVerify():
    users = input("Please type in your new username: ")
    if(os.path.exists(users) == False):
        os.mkdir(users)
        print("New " + users + " created")
        dateVerify(users)
    else:
        print("User already exists")
        newUserVerify()

def userVerify():
    users = input("Please type in your username: ")
    if(os.path.exists(users) == False):
        print("This user does not exist. Try again")
        userVerify()
    else:
        print("User verified")
        dateVerify(users)
    
def dateVerify(users):
    userStatus = input(f"Would you like to add Caloried for {nowMonth} {nowDate} (yes/no): ") 
    if(userStatus.lower() == "yes"):
        menu(users, nowDate)
    elif(userStatus.lower() == "no"):
        print("What date would you like to add Calories to")
        print(f"Month:{nowMonth}")
        date = input("Date: ")
        if ((date.isnumeric() == False) or (date > nowDate)):
            print("Can't input data for the future")
            dateVerify(users)
        else:
            menu(users, date)
    else:
        print("Please enter yes or no")
        dateVerify(users)

def calorieAdder(user, date, nowDate):
    counter = 0
    os.chdir(mainPath)
    os.chdir(user)
    if(os.path.exists(nowMonth) == True):
        os.chdir(nowMonth)
    else:
        os.mkdir(nowMonth)
        os.chdir(nowMonth)
    print("Please add your calories in this format (Item-Quantity)\nIf you are a new user please add calories in this format (Item-Quantity-Calorie)")
    count = input("Please input the amount items you want to input: ")
    count = int(count)
    itemArray = []
    quantityArray = []
    caloriesArray = []
    perArray = []
    totalArray = []
    while (counter != count):
        item = input("Item: ")
        itemArray.append(item)
        quantity = input("Quantity: ")
        quantity = int(quantity)
        quantityArray.append(quantity)
        calories = input("Calories: ")
        calories = int(calories)
        caloriesArray.append(calories)
        perAmount = input("Per amount: ")
        perAmount = int(perAmount)
        perArray.append(perAmount)
        total = (quantity/perAmount)*calories
        totalArray.append(total)
        counter += 1
        if(counter == count):
            titledColumn = ({"Item": itemArray, "Quantity": quantityArray, "Calories": caloriesArray, "Per Amount": perArray, "Total": totalArray})
            data = pd.DataFrame(titledColumn)
            if(os.path.exists(date)):
                data.to_csv(date, mode='a', header=False, index=False)
                print("Added to database")
                totalCalculator(user, date, nowDate)
                menu(user, nowDate)
            else:
                data.to_csv(date, index=False)
                totalCalculator(user, date, nowDate)
                menu(user, nowDate)

def grapher(user):
    print(f"This will graph for {user}")

def weightAdder(user, date):
    print(f"This will add weight for {user} for the date of {date}") 

def totalMonthTable(user):
    os.chdir(mainPath)
    os.chdir(user)
    os.chdir(nowMonth)
    print(f"This is the total Calories for {nowMonth}")
    df = pd.read_csv('Total.csv')
    print(df.to_markdown())

def totalCalculator(user, date, nowDate):
    df = pd.read_csv(date)
    sumTotal = df['Total'].sum()
    totaldata = ({"Date": [nowDate], "Total": [sumTotal]})
    dw = pd.DataFrame(totaldata)
    if(os.path.exists('Total.csv')):
        dw.to_csv('Total.csv', mode='a', header=False, index=False)
    else:
        dw.to_csv('Total.csv', index=False)

def tablePrinter(user, date):
    os.chdir(mainPath)
    os.chdir(user)
    os.chdir(nowMonth)
    print(date)
    print(f"This will print your calorie table for {date}")
    df = pd.read_csv(date)
    print(df.to_markdown())

def menu(user, date):
    todayDate = nowMonth + date 
    print("-----------------------------------")
    print("Welcome to the Menu.") 
    print("Press 1 to display a graph")
    print("Press 2 to add more calores")
    print("Press 3 to add a weight")
    print(f"Press 4 to get a table of {todayDate}")
    print(f"Press 5 to get a table for total calories for {nowMonth}")
    print("Press q to quit")
    menu = input("Please type your choice here: ")
    print("----------------------------------")
    match menu:
        case'1':
            grapher(user)
        case'2':
            calorieAdder(user, todayDate, date)
        case'3':
            weightAdder(user, todayDate)
        case'4':
            tablePrinter(user, todayDate)
        case'5':
            totalMonthTable(user)            
        case'q':
            print("Thank you for using the Calorie Counter")
        case default:
            print("Unaviable menu choice. Please try again")
            menu(user, date)

print("Welcome to your personal Calorie Counter")
print("----------------------------------")
userStatus = input("Are you a new user (yes/no)")

while(userStatus.lower() != ("yes") or ("no")):
    if(userStatus.lower() == "yes"):
        print("Welcome new user")
        newUserVerify()
        break
    elif(userStatus.lower() == "no"):
        print("Welcome back")
        userVerify()
        break
    else:
        userStatus = input("Are you a new user (yes/no)")
        
