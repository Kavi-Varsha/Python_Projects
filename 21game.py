"""21 Number Game
Description
The 21 Number Game is a simple mathematical strategy game played between a user and the computer.

Players take turns adding 1, 2, or 3 to a running total, starting from 0.
The player who reaches 21 loses the game.
The computer follows a winning strategy to try and avoid reaching 21.
This Python program allows users to play against the computer, which uses a strategic algorithm to maximize its chances of winning.

How to Play
The game randomly decides who goes first (You or the Computer).
On your turn, enter a number: 1, 2, or 3.
The total sum increases with each move.
The player who reaches 21 loses.
The game continues until either the player or the computer loses.
"""

import random

def game():
    """
    This function runs the 21 Number Game where a player and a computer take turns.
    The goal is to avoid making the total reach 21. Whoever reaches 21 loses.
    """
    
    total = 0  # Initial sum is 0
    player_turn = random.choice([True, False])  # Randomly decide who starts first

    if player_turn:
        print("You start.")
    else:
        print("Computer starts.")

    print("Total is:", total)

    while total < 21:
        if player_turn:
            # Player's turn
            try:
                player_num = int(input("Enter a number (1, 2, or 3): "))  # Take input
            except ValueError:
                print("Invalid input. Please enter a number between 1, 2, or 3.")
                continue  # Ask again if input is not a number
            
            if player_num not in [1, 2, 3]:  # Ensure input is valid
                print("Enter a valid number (1, 2, or 3).")
                continue
            
            total += player_num  # Add player input to total
            print(f"You chose {player_num}. Total is now {total}.")

            if total >= 21:
                print("You lose! Computer wins!")
                break  # Game over
            
        else:
            # Computer's turn
            if total % 4 == 0:
                computer_num = random.choice([1, 2, 3])  # Random move when on multiple of 4
            else:
                computer_num = 4 - (total % 4)  # Winning strategy to avoid losing

            total += computer_num  # Add computer move to total
            print(f"Computer chooses {computer_num}. Total is now {total}.")

            if total >= 21:
                print("Computer loses! You win!")
                break  # Game over
        
        # Toggle turn
        player_turn = not player_turn

# Run the game
game()
