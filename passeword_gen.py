import random
import string

print("Welcome to password Generator:")

length = int(input("Enter length of Password:"))

letter = ""

x = input("If you want Letters(yes/no):")
if( x == "yes"):
    letter = string.ascii_letters

y = input("If you want Digits(yes/no):")
if( y == "yes"):
    letter += string.digits

z = input("If you want Speacial Characters(yes/no):")
if( z == "yes"):
    letter += string.punctuation

if(letter == ""):
    print("No character type selected -- deafault to letters")
    letter = string.ascii_letters

password = ""

for el in range(length):
    next_pass = random.choice(letter)
    password += next_pass

print("The Passoword = ", password)












