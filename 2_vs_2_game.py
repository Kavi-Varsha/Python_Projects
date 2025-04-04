import random  # Importing random module for attack damage calculation

# Base Character Class
class Character:
    def __init__(self, name, strength, health):
        """
        Initializes a character with name, strength, and health.
        """
        self.name = name
        self.strength = strength
        self.health = health

    def attack(self):
        """
        Generates a random attack damage within a range of strength ±3.
        """
        return random.randint(self.strength - 3, self.strength + 3)

    def hit(self, points):
        """
        Reduces health based on the attack damage received.
        Ensures health does not go below zero.
        """
        self.health = max(0, self.health - points)

    def isalive(self):
        """
        Checks if the character is still alive (health > 0).
        """
        return self.health > 0

    def display(self):
        """
        Displays character details.
        """
        print(f"Name: {self.name}\nClass: {self.__class__.__name__}\nStrength: {self.strength}\nHealth: {self.health}\n")


# Subclasses for Different Character Types with Predefined Strength and Health
class Warrior(Character):
    def __init__(self, name):
        """
        Warrior class with high strength and health.
        """
        super().__init__(name, strength=15, health=120)


class Soldier(Character):
    def __init__(self, name):
        """
        Soldier class with medium strength and health.
        """
        super().__init__(name, strength=12, health=100)


class Servant(Character):
    def __init__(self, name):
        """
        Servant class with lower strength and health.
        """
        super().__init__(name, strength=10, health=80)


# Battle Class to Handle Combat Between Two Characters
class Battle:
    def __init__(self, char1, char2):
        """
        Initializes the battle with two characters.
        """
        self.char1 = char1
        self.char2 = char2

    def fight(self):
        """
        Simulates a turn-based fight between two characters until one is defeated.
        """
        print(f"\n⚔️ Battle Begins: {self.char1.name} ({self.char1.__class__.__name__}) vs {self.char2.name} ({self.char2.__class__.__name__})\n")

        round_number = 1  # Track rounds

        while self.char1.isalive() and self.char2.isalive():
            print(f"Status After Round {round_number}:\n")

            # Character 1 attacks Character 2
            damage = self.char1.attack()  # Generate attack damage
            self.char2.hit(damage)  # Apply damage to opponent
            print(f"{self.char1.name} attacked {self.char2.name} with {damage} damage.")
            print(f"Health({self.char2.name}): {self.char2.health}\n")

            # Check if Character 2 is defeated
            if not self.char2.isalive():
                print(f"\n🏆 Battle Over! {self.char1.name} ({self.char1.__class__.__name__}) Wins!\n")
                return  # End battle

            # Character 2 attacks Character 1
            damage = self.char2.attack()  # Generate attack damage
            self.char1.hit(damage)  # Apply damage to opponent
            print(f"{self.char2.name} attacked {self.char1.name} with {damage} damage.")
            print(f"Health({self.char1.name}): {self.char1.health}\n")

            # Check if Character 1 is defeated
            if not self.char1.isalive():
                print(f"\n🏆 Battle Over! {self.char2.name} ({self.char2.__class__.__name__}) Wins!\n")
                return  # End battle

            round_number += 1  # Increment round count


# Create Characters
char1 = Warrior("Thor")  # Create a Warrior character
char2 = Servant("James")  # Create a Servant character

# Print Character Details
char1.display()  # Display Warrior details
char2.display()  # Display Servant details

# Start Battle
b1 = Battle(char1, char2)
b1.fight()  # Begin the fight
