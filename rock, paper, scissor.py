import random

options = ["rock" , "paper", "scissor"]
play = True
while play:

    player = None
    ai = random.choice(options)

    player = input("Enter Your Choice:")

    print(f"Player : {player}")
    print(f"Computer : {ai}")

    if (ai == player):
        print("Its a tie")
    elif ( player == "rock" and ai == "scissor"):
        print("You Win!")
    elif ( player == "paper" and ai == "rock"):
        print("You Win!")
    elif ( player == "scissor" and ai == "paper"):
        print("You Win!")

    else:
        print("You Lose")

    again = input("Play Again? (y/n) :")
    if not again == "y":
        play = False

print("Thanks for Playing")











