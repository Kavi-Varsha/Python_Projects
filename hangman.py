import random

# Function to restart the game
def play_game():
    l = ["hello", "mango", "orange"]
    word = random.choice(l)
    guess = 0
    attempt = len(word) + 2
    char = []
    print("\nThe length of the word is:", len(word))

    while guess < attempt:
        print("\nEnter a character:")
        user_input = input().lower()

        # Check for duplicate guesses
        if user_input in char:
            print("You have already guessed that letter.")
            continue
        else:
            char.append(user_input)

        # Build the display string
        display = ""
        for i in word:
            if i in char:
                display += i  
            else:
                display += "_"  

        print("Current progress:", display)

        # Win condition
        if display == word:
            print(f"Congratulations! You guessed the word in {len(char)} guesses.")
            print("Do you want to try again? (yes or no)")
            if input().lower() == "yes":
                play_game()  # Restart the game
            else:
                print("Thanks for playing! Goodbye.")
                return  # End the game

        # Incorrect guess handling
        if user_input not in word:
            guess += 1
            print(f"Wrong guess! Attempts left: {attempt - guess}")

    # If out of attempts
    print("\nGame Over! The correct word was:", word)

# Start the game
play_game()
