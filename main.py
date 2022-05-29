import os
import datetime

x = datetime.datetime.now()
todayDate = x.strftime("%B %d")
nowDate = x.strftime("%d")
nowMonth = x.strftime("%B")

def newUserVerify():
    users = input("Please type in your new username: ")
    if(os.path.isfile(users) == False):
        fp = open(users, "w")
        fp.write('Calorie Counter')
        fp.close()
        print("New " + users + " created")
    elif(os.path.isfile(users) == True):
        print("User already exists")
        newUserVerify()
    else:
        print("User " + users + " does not exist")
        newUserVerify()

def userVerify():
    users = input("Please type in your username: ")
    if(os.path.isfile(users) == True):
        print("User Verified")
        calorieAdder(users)
    else:
        print("User " + users + " does not exist")
        userVerify()

def calorieAdder(users):
    userStatus = input("Would you like to add Caloried for " + nowMonth + " " + nowDate + " (yes/no): ") 
    if(userStatus.lower() == "yes"):
        print("Please type in the format of (Item-Calories)")
    elif(userStatus.lower() == "no"):
        print("What date would you like to add Calories to")
        month = input("Month: ")
        date = input("Date: ")

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
        
