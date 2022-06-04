import os
import datetime

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
    userStatus = input("Would you like to add Caloried for " + nowMonth + " " + nowDate + " (yes/no): ") 
    if(userStatus.lower() == "yes"):
        calorieAdder(users, nowDate)
    elif(userStatus.lower() == "no"):
        print("What date would you like to add Calories to")
        print("Month: " + nowMonth)
        date = input("Date: ")
        if ((date.isnumeric() == False) or (date > nowDate)):
            print("Can't input data for the future")
            dateVerify(users)
        else:
            calorieAdder(users, date)
    else:
        print("Please enter yes or no")
        dateVerify(users)
    
def calorieAdder(users, date):
    todayDate = nowMonth + date
    os.chdir(users)
    fp = open(todayDate, "w")
    fp.write(todayDate)
    fp.close()

print("Welcome to your personal Calorie Counter\n")
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
        
