# Importing the module that equips me with functions that can be used to generate random numbers
import random

# Getting the information from the user
print("Welcome to the PyPassword Generator!")
nr_characters = int(input("How many characters would you like in your password?\n"))
nr_passwords = int(input("How many passwords would you like generated?\n"))
alphanumeric = input("Would you like to remove special symbols and only use alphanumeric characters? (less secure but more compatible)\nPress enter to continue normally, or press Y for numbers and letters only.\n").lower()

# Creating a list of generally accepted characters
alphanumeric_symbols = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
]
character_list = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '='
]

# Declaring the variable that will later have random characters appended to it and end up being printed
password = ""

if alphanumeric == "":
    if nr_characters <= 500 or nr_passwords <= 500:
        for passwords in range(nr_passwords): # Loops the script for as many passwords as the user wants generated
            for character in range(nr_characters): # Loops the script for as many characters as the user wants
                password += random.choice(character_list) # Generates the password one character at a time
            print(password) # After that password has generated, this will print the password
            password = "" # Resets the password so when the second for loop restarts, it has a clear canvas/
    else:
        print("You can only generate up 500 passwords and/or characters at a time. Please try again.")
elif alphanumeric == "y" or alphanumeric == "Y":
    if nr_characters <= 500 or nr_passwords <= 500:
        for passwords in range(nr_passwords): # Loops the script for as many passwords as the user wants generated
            for character in range(nr_characters): # Loops the script for as many characters as the user wants
                password += random.choice(alphanumeric_symbols) # Generates the password one character at a time
            print(password) # After that password has generated, this will print the password
            password = "" # Resets the password so when the second for loop restarts, it has a clear canvas/
    else:
        print("You can only generate up 500 passwords and/or characters at a time. Please try again.")
else:
    print("You didn't press Y or enter, resorting to default (with special symbols)\n")
    if nr_characters <= 500 or nr_passwords <= 500:
        for passwords in range(nr_passwords): # Loops the script for as many passwords as the user wants generated
            for character in range(nr_characters): # Loops the script for as many characters as the user wants
                password += random.choice(character_list) # Generates the password one character at a time
            print(password) # After that password has generated, this will print the password
            password = "" # Resets the password so when the second for loop restarts, it has a clear canvas/
    else:
        print("You can only generate up 500 passwords and/or characters at a time. Please try again.")
