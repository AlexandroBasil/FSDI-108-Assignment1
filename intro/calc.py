""" 
System: simple calculator
Author: Alex Garcia
Functionality:
    -Sum
    -Subtract
    -Multiply
    -Divide
"""

# imports
from display import print_menu

# global variables


# functions


# plain instructions

opt = ""
while(opt != "q"):
    print_menu()
    opt = input("Choose an option: ")
    if(opt == "q"):
        break

    try:
        num1 = float(input("Provide num1: "))
        num2 = float(input("Provide num2: "))
    except:
        print("Invalid input, please try again")
        continue

    if(opt == "1"):
        print(f"The result is: {num1 + num2}")

    elif(opt == "2"):
        print(f"The result is: {num1 - num2}")

    elif(opt == "3"):
        print(f"The result is: {num1 * num2}")

    elif(opt == "4"):
        if(num2 == 0):
            print("Error: Cannot divide by zero, please try again")
        else:
            print(f"The result is: {num1 / num2}")
    
    input("Press enter to continue...")

print("Thank You for using my calculator!")
