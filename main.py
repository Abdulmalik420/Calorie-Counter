import os
import datetime
import csv

x = datetime.datetime.now()
nowDate = x.strftime("%d")
nowMonth = x.strftime("%B")

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
    
def calorieAdder(users, date):
    todayDate = nowMonth + date
    os.chdir(users)
    print("Please add your calories in this format (Item-Quantity)\nIf you are a new user please add calories in this format (Item-Quantity-Calorie)")
    print("When you finish inputing the calories please input |q| in order to quit")
    with open(todayDate, 'w', encoding = 'UTF8', newline = '') as f:
        writer = csv.writer(f)
        header = ['Item', 'Quantity', 'Calories']
        choose = input()
        writer.writerow(header)
        while choose!='q':
            calories = choose.split("-")
            writer.writerow(calories)
            choose = input()

def grapher(user):
    print(f"This will graph for {user}")

def weightAdder(user, date):
    print(f"This will add weight for {user} for the date of {date}") 

def calorieCal(user, date):
    print(f"This will calculate the total calories for {nowMonth} {date}")

def menu(user, date):
    print("-----------------------------------")
    print("Welcome to the Menu.") 
    print("Press 1 to display a graph")
    print("Press 2 to add more calores")
    print("Press 3 to add a weight")
    print(f"Press 4 to get a summary for {nowMonth} {date}")
    menu = input("Please type your choice here: ")
    print("----------------------------------")
    match menu:
        case'1':
            grapher(user)
        case'2':
            calorieAdder(user, date)
        case'3':
            weightAdder(user, date)
        case'4':
            calorieCal(user, date)
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
        
