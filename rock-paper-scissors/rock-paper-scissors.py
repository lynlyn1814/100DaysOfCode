# Importing the module that allows me to generate random values for the computer's turn
import random

# Storing the ASCII art into variables for easier use later
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

trophy = " .-=========-.\r\n \\\'-=======-\'/\r\n _|   .=.   |_\r\n((|  {{1}}  |))\r\n \\|   /|\\   |/\r\n  \\__ \'`\' __/\r\n    _`) (`_\r\n  _/_______\\_\r\n /___________\\"

gravestone = "    _____\r\n  /~/~   ~\\\r\n | |       \\\r\n \\ \\        \\\r\n  \\ \\        \\\r\n --\\ \\       .\\\'\'\r\n--==\\ \\     ,,i!!i,\r\n    \'\'\"\'\',,}{,,"

you_won = " _   _  ___  _   _  __      _____  _ __  \r\n| | | |/ _ \\| | | | \\ \\ /\\ / / _ \\| \'_ \\ \r\n| |_| | (_) | |_| |  \\ V  V / (_) | | | |\r\n \\__, |\\___/ \\__,_|   \\_/\\_/ \\___/|_| |_|\r\n  __/ |                                  \r\n |___/                                   "

you_lost = "                    | |         | |  \r\n _   _  ___  _   _  | | ___  ___| |_ \r\n| | | |/ _ \\| | | | | |/ _ \\/ __| __|\r\n| |_| | (_) | |_| | | | (_) \\__ \\ |_ \r\n \\__, |\\___/ \\__,_| |_|\\___/|___/\\__|\r\n  __/ |                              \r\n |___/"

its_a_tie = " _ _   _               _   _      \r\n(_) | ( )             | | (_)     \r\n _| |_|/ ___    __ _  | |_ _  ___ \r\n| | __| / __|  / _` | | __| |/ _ \\\r\n| | |_  \\__ \\ | (_| | | |_| |  __/\r\n|_|\\__| |___/  \\__,_|  \\__|_|\\___|"

# Turning the options into a list
options = ["Rock", "Paper", "Scissors"]

# Getting the user's choice
user_choice = input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors.\n")

# Turning the user's choice into one of the options
if user_choice == "0":
    user_choice = options[0]
elif user_choice == "1":
    user_choice = options[1]
elif user_choice == "2":
    user_choice = options[2]
else:
    print("Something went wrong...")

# Generating the computer's choice
computer_choice = random.choice(options)

# Printing the computer's choice
if computer_choice == options[0]:
    print(f"\nComputer chose: {rock}\n")
elif computer_choice == options[1]:
    print(f"\nComputer chose: {paper}\n")
elif computer_choice == options[2]:
    print(f"\nComputer chose: {scissors}\n")
else:
    print("Something went wrong...")

# Printing the user's choice
if user_choice == options[0]:
    print(f"You chose: {rock}")
elif user_choice == options[1]:
    print(f"You chose: {paper}")
elif user_choice == options[2]:
    print(f"You chose: {scissors}")
else:
    print("Something went wrong...")

# Determining and printing the winner along with some ASCII art

if user_choice == options[0]:
    if computer_choice == options[1]:
        print(f"{gravestone}\n{you_lost}")
    elif computer_choice == options[2]:
        print(f"{trophy}\n{you_won}")
    else:
        print(its_a_tie)
else:
    print("Something went wrong...")

if user_choice == options[1]:
    if computer_choice == options[2]:
        print(f"{gravestone}\n{you_lost}")
    elif computer_choice == options[0]:
        print(f"{trophy}\n{you_won}")
    else:
        print(its_a_tie)
else:
    print("Something went wrong...")

if user_choice == options[2]:
    if computer_choice == options[0]:
        print(f"{gravestone}\n{you_lost}")
    elif computer_choice == options[1]:
        print(f"{trophy}\n{you_won}")
    else:
        print(its_a_tie)
else:
    print("Something went wrong...")
