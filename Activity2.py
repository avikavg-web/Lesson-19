import random
options = ["rock", "paper", "scissor"]
computerchoice = random.choice(options)
userchoice = input("Choose between rock, paper, and scissors: ")
while True:
    if computerchoice == userchoice:
        print("It's a tie")
    elif computerchoice == "rock":
        if userchoice == "paper":
            print("The user won")
        else:
            print("The computer won")
    elif computerchoice == "paper":
        if userchoice == "rock":
            print("The computer won")
        else:
            print("The user won")
    elif computerchoice == "scissors":
        if userchoice == "rock":
            print("The user won")
        else:
            print("The computer won")
    playagain = input("Play again?")
    if playagain == "no":
        break
    




    