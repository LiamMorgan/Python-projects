#Prompts the user to input a number between 1-100, and replies with "Higher, Lower, Correct" depending on answer.
import random

def main():
    rand = random.randint(0,100)
    while True:
        try:
            user = int(input("Enter the number between 1-100.\n"))
        except ValueError:
            print("Must be a number.")
            main()
        if user < rand:
            print("Higher.")
        elif user > rand:
            print("Lower.")
        elif user == rand:
            print("Correct.")
            break
        else:
            print("Enter a number.\n")

def askX():
    user = input("Enter Y play or N to exit.\n")
    if user == "y" or user == "Y":
        main()
        askX()
    elif user == "n" or user == "N":
        quit()

askX()
