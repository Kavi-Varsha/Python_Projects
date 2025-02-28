import random

def word_scramble_game():
    while True:
        words = ["hello", "mango", "orange", "python", "elephant", "giraffe", "sunflower", "butterfly", "keyboard", "mountain"]
        word = random.choice(words)  # Select a random word
        word_list = list(word)  # Convert string to list
        random.shuffle(word_list)  # Shuffle the list
        scrambled_word = "".join(word_list)  # Convert back to string
        
        print("\nThe scrambled word is:", scrambled_word)
        print("You have 3 attempts to guess the original word.")
        
        guesses = 0
        attempts = 3
        
        while guesses < attempts:
            guessed_word = input("Guess the word: ").lower()
            
            if guessed_word == word:  # Check against the original word, not scrambled
                print(f"Correct! You guessed the word '{word}' in {guesses + 1} attempts.")
                break
            else:
                print("Incorrect. Try again!")
                guesses += 1

        if guesses == attempts:
            print(f"You lost! The correct word was '{word}'.")
        
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break  # Exit the loop if the player does not want to continue

word_scramble_game()
