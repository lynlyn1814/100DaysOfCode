import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

lives = 6 # Decreases with incorrect guesses
correct_letters = [] # Stores letters you guessed correctly
previous_guesses = [] # Stores every guess you've made
game_over = False # Used as the condition for the main while loop, allowing for multiple guesses
placeholder = "" # Placeholder for the initial string of underscores to show how many characters are in the randomly chosen word
chosen_word = random.choice(word_list) # Generates a random word from an imported list and stores it to the chosen_word variable
word_length = len(chosen_word) # Calculates the length of the word for easier use of the value


print(logo) # Prints the hangman logo

for position in range(len(chosen_word)): # For every character in the chosen word, it adds one underscore to the currently empty 'placeholder' variable
    placeholder += "_"
print(f"Word to guess: {placeholder} ({word_length} characters)") # Prints the underscores and the amount of characters in the word
placeholder = ""

# Finally, the actual logic of the game
while not game_over: # Repeats once every time you guess until game_over is true, which happens when you guess incorrectly 6 times
    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower() # Takes your guess and makes it lowercase

    if guess in previous_guesses: # Checks if you've already guessed a letter
        print("You already guessed that letter!")
    previous_guesses += guess # This comes after the check, otherwise by then the guess you just made will already be in the previous_guesses list

    display = ""
    for letter in chosen_word: # Creates the new hint, including any correctly guessed hints' position(s)
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display) # Prints the new hint

    if guess not in chosen_word: # Checks if your guess is incorrect. If so, it changes your amount of lives, then informs you
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0: # Checks if you're out of lives. If so, stops the while loop by setting game_over to false and then tells you what the word you were trying to guess was
            game_over = True
            print(f"***********************YOU LOSE**********************\nThe word was \"{chosen_word}\"")

    if "_" not in display: # Checks if there are any missing letters left. If not, then that means you win.
        game_over = True
        print(f"***********************YOU WIN**********************\nThe word was \"{chosen_word}\"")

    print(stages[lives]) # At the end of every guess, it shows the stage of hangman you're on
