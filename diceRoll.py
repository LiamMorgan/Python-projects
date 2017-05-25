import random

while True:
    user = input("Enter Y to roll the dice, N to close program\n")
    if user == "y" or user == "Y" :
        print(random.randint(1,6))
    elif user == "n" or user == "N" :
        break
    else:
       user = input("Not valid input, enter Y or N\n")
for x in range(10) :
quit()
