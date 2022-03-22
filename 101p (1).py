import random
from urllib import response

while response=="y":
    no=random.randint(0,6)

    if(no==1):
        print("*")

    elif(no==2):
        print("**")
    
    elif(no==3):
        print("***")

    elif(no==4):
        print("****")

    elif(no==5):
        print("*****")

    elif(no==6):
        print("******")


response = input("Enter the time in number of seconds: ")
    