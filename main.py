import os
import time

def newUserVerify(users):
    if(os.path.isfile(users) == False):
        fp = open(users, "w")
        fp.write('Calorie Counter')
        fp.close()
    else:
        print("This user already exists")

def userVerify():
    user = input("Please type in you username\n")
    if(os.path.isfile(user) == True):
        print("User Verified")
        verifier = True
    else:
        print("User " + user + " does not exist")
        userVerify()

verifier = False
print("Welcome to your personal Calorie Counter\n")
userStatus = input("Are you a new user (yes/no)")

while(userStatus.lower() != ("yes") or ("no")):
    if(userStatus.lower() == "yes"):
        print("Welcome new user")
        user = input("Please type in your new username\n")
        newUserVerify(user)
        break
    elif(userStatus.lower() == "no"):
        print("Welcome back")
        userVerify()
        if(verifier == True):
            print("Would you like to add Calories for " + time.asctime())
        break
    else:
        userStatus = input("Are you a new user (yes/no)")
        
