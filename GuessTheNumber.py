import random

target = random.randint(1,100)
while(True):
    userChoice = (input("Guess the target or Quit(Q): "))
    if(userChoice == "Q"):
        print("You Quit the game.")
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("WOW Perfect guess! Sucessful Guessing!!")
        print(f"The number was {target}")
        break
    elif(userChoice < target):
        print("Your guess is too small. Guess greater no...")    
    else:
        print("Your guess is too big:Guess smaller no...")

print("------GAME OVER------")