import random

def play_game():
    """Function to start and restart the word guessing game."""
    while True:  # Loop to allow restarting the game
        words = ["hello", "mango", "orange", "python", "elephant", "giraffe", "sunflower", "butterfly", "keyboard", "mountain"]
        word = random.choice(words)  # Select a random word
        guess = 0  # Track incorrect guesses
        max_attempts = len(word) + 2  # Total allowed attempts
        guessed_chars = []  # Store guessed letters

        print("\nThe length of the word is:", len(word))

        while guess < max_attempts:
            print("\nEnter a character:")
            user_input = input().lower()

            # Ensure input is a single character
            if len(user_input) != 1 or not user_input.isalpha():
                print("Invalid input. Please enter only one letter.")
                continue

            # Check for duplicate guesses
            if user_input in guessed_chars:
                print("You have already guessed that letter.")
                continue

            guessed_chars.append(user_input)  # Add input to guessed list

            # Build the display string
            display = ""
            for char in word:
                if char in guessed_chars:
                    display += char  
                else:
                    display += "_"

            print("Current progress:", display)

            # Win condition
            if display == word:
                print(f"Congratulations! You guessed the word in {len(guessed_chars)} attempts.")
                break

            # Incorrect guess handling
            if user_input not in word:
                guess += 1
                print(f"Wrong guess! Attempts left: {max_attempts - guess}")

        # If out of attempts
        if display != word:
            print("\nGame Over! The correct word was:", word)

        # Ask to restart the game
        retry = input("Do you want to play again? (yes or no): ").lower()
        if retry != "yes":
            print("Thanks for playing! Goodbye.")
            break  # Exit loop and end game

# Start the game
play_game()
