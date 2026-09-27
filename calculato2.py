
import math

print("Welcome To Calculator")

while True:

    x = float(input("Enter Number:"))
    function = input("Enter the operator (+,-,x,/,%,^,sin,cos,tan,!):")
   

    if(function == "+"):
        y = float(input("Enter Number:"))
        result = x + y
    elif(function == "-"):
        y = float(input("Enter Number:"))
        result = x - y
    elif(function == "x"):
        y = float(input("Enter Number:"))
        result = x * y 

    elif(function == "/"):
        y = float(input("Enter Number:"))
        if(y != 0):
            result = x / y
        else:
            result ="Invalid, Cannot Divide by 0"

    elif(function == "%"):
        y = float(input("Enter Number:"))
        result = (x / y)*100

    elif(function == "^"):
        y = float(input("Enter Number:"))
        result = x**y

    elif(function == "!"):
        if (x >= 0 and x == int(x)):
            result = math.factorial(int(x))
        else:
            result = "Factorial requries non-negative Numbers"

    elif(function == "sin"):
        result = math.sin(math.radians(x))

    elif(function == "cos"):
        result = math.cos(math.radians(x))

    elif(function == "tan"):
        result = math.tan(math.radians(x))
    
    else:
        print("Invalid Operation")

    print("Result =",result)

    choice = input("Do you want to calculate again ?(yes/no):")
    if(choice.lower() != "yes"):

        print("Thanks For Using Calculator.")
        print("Calculator Closed")
        break


        