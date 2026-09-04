import random

print("Welcome to the Number Guessing Game")

high = int(input("Enter Higher Bond :"))
low = int(input("Enter lower Bond :"))

print("You have 7 chances to Win the Game \n")

number = random.randint(low , high)
x = 0 
y = 7

while x < y:
    guess = int(input("Enter Guess : "))
    x += 1

    if guess > number :
        print("Number is too high and You have", y - x, "chances Left") 
 
    elif guess < number :
        print("Number is too low and You have", y - x, "chances Left")
    else:
        print("You have guessed the number in", y - x ,"chances & You have Won !")
        break 




