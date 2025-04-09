'''Features of the Game:
- Interactive battles: The player fights enemies using attack, block, or heal moves.
- Dynamic storytelling: Choices made during the adventure lead to different outcomes.
- Randomized mechanics: Enemy attacks and player actions have random effects, keeping the game unpredictable.
- Health points (HP): Players must manage their HP wisely to survive'''


import random
import time

# Game introduction
def game_intro():
    print("Welcome, adventurer, to the world of Eldoria!")
    time.sleep(1)
    print("A land filled with mysteries, dangers, and endless possibilities.")
    time.sleep(1)
    print("Your journey begins now...\n")

# Player stats
player = {
    "name": "",
    "hp": 100,
    "inventory": []
}

# Enemy stats
enemies = [
    {"name": "Goblin", "hp": 30},
    {"name": "Dark Knight", "hp": 50},
    {"name": "Dragon", "hp": 100}
]

# Battle function
def battle(enemy):
    print(f"\nA {enemy['name']} appears!")
    time.sleep(1)
    print(f"It has {enemy['hp']} HP.\n")
    
    while enemy['hp'] > 0 and player['hp'] > 0:
        print("Your moves:")
        print("1. Attack")
        print("2. Block")
        print("3. Heal\n")
        
        move = input("Choose your move (1/2/3): ")
        if move == "1":
            damage = random.randint(10, 25)
            enemy['hp'] -= damage
            print(f"You attacked and dealt {damage} damage!")
        elif move == "2":
            block = random.randint(5, 15)
            print(f"You blocked! Enemy attack is reduced by {block} points.")
        elif move == "3":
            heal = random.randint(10, 20)
            player['hp'] += heal
            print(f"You healed yourself for {heal} HP!")
        else:
            print("Invalid move! You lose your turn.")
        
        if enemy['hp'] > 0:
            enemy_damage = random.randint(10, 20)
            player['hp'] -= max(0, enemy_damage - block)
            print(f"The {enemy['name']} attacks and deals {enemy_damage} damage!")
        
        print(f"Your HP: {player['hp']}")
        print(f"{enemy['name']}'s HP: {enemy['hp']}\n")
        time.sleep(1)
    
    if player['hp'] <= 0:
        print("\nYou have been defeated... Game Over.")
        return False
    elif enemy['hp'] <= 0:
        print(f"\nYou defeated the {enemy['name']}! Congratulations!")
        return True

# Adventure function
def adventure():
    print("\nYou find yourself at a crossroads.")
    time.sleep(1)
    print("1. Explore the dark forest.")
    print("2. Enter the abandoned castle.")
    print("3. Venture into the mysterious cave.\n")
    
    choice = input("Where do you want to go? (1/2/3): ")
    if choice == "1":
        print("\nThe forest is eerie and full of hidden dangers.")
        time.sleep(1)
        if battle(random.choice(enemies)) == False:
            return False
    elif choice == "2":
        print("\nThe castle is ancient, and you hear strange noises...")
        time.sleep(1)
        if battle(random.choice(enemies)) == False:
            return False
    elif choice == "3":
        print("\nThe cave is dark, but it holds secrets.")
        time.sleep(1)
        if battle(random.choice(enemies)) == False:
            return False
    else:
        print("Invalid choice. You stumble and lose precious time.")
        player['hp'] -= 10
        print(f"Your HP: {player['hp']}\n")
        if player['hp'] <= 0:
            print("You have run out of time... Game Over.")
            return False
    return True

# Main game loop
def main_game():
    game_intro()
    player['name'] = input("Enter your name, adventurer: ")
    print(f"\nWelcome, {player['name']}! Prepare for your quest...\n")
    while player['hp'] > 0:
        if adventure() == False:
            break
        print("\nDo you want to continue your adventure?")
        choice = input("Type 'yes' to continue or 'no' to end your journey: ")
        if choice.lower() != "yes":
            print("\nYour journey ends here. Farewell, brave adventurer!")
            break
    print("\nThanks for playing!")

# Run the game
main_game()
