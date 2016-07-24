import time
import random

constant= 1
FirstRun= True

def Intro():
    print("Hello and welcome to coin flipper, do you wish to flip the coin? (yes or no)")

    def CoinToss():
        print("you flip the coin")
        time.sleep(1)
        print("and the result is...")
        time.sleep(1)
        result= random.randint(1,2)
        if result == 1:
            print("heads")
        if result == 2:
            print("tails")

while constant ==1:
    if FirstRun == True:
     Intro()
     FirstRun = False

     else:
         Answer = input()
         if Answer== "yes":
             CoinToss()
             print("Do you want to flip it again? (yes or no)")

            else:
                exit()
     
