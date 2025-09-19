# Imported sys so I can end the program if the user inputs an invalid answer-
# - a bit preemptive for day 3 but I might as well
import sys

print("Welcome to Python Pizza Deliveries! Inputs are case sensitive.")

# Asks what size pizza the user wants
size = input("What size pizza do you want? S, M or L: ")
if size == "L":
    print("You will get a large pizza!")
elif size == "M":
    print("You will get a medium pizza!")
elif size == "S":
    print("You will get a small pizza!")
else:
    print("Your input was invalid. Please try again and make sure it's capitalised!")
    sys.exit()

# Asks if the user wants
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    print("Your pizza will have pepperoni!")
elif pepperoni == "N":
    print("Your pizza will have no pepperoni!")
else:
    print("Your input was invalid. Please try again and make sure it's capitalised!")
    sys.exit()

# Asks if the user wants extra cheese
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    print("Your pizza will have extra cheese!")
elif extra_cheese == "N":
    print("Your pizza will not have extra cheese!")
else:
    print("Your input was invalid. Please try again and make sure it's capitalised!")
    sys.exit()

# Initialises and sets starting point for the bill
bill = 0

# Checks inputs and calculates final bill
if size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
else:
    print("Oops! An error has occurred, please try again.")

# Prints the final bill
print(f"Your final bill is: ${bill}")
