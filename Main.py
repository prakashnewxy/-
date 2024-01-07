
import random

class Player:
    def __init__(self, name, health=100, inventory=None):
        self.name = name
        self.health = health
        self.inventory = inventory or []

    def display_inventory(self):
        print(f"{self.name}'s Inventory: {', '.join(self.inventory)}")

class Location:
    def __init__(self, name, description, items=None, enemies=None):
        self.name = name
        self.description = description
        self.items = items or []
        self.enemies = enemies or []

    def explore(self, player):
        print(f"\nYou are at {self.name}. {self.description}")

        # Display available items in the location
        if self.items:
            print("Items available:")
            for item in self.items:
                print(f"- {item}")

        # Display enemies in the location
        if self.enemies:
            print("Enemies present:")
            for enemy in self.enemies:
                print(f"- {enemy}")

        # Let the player decide what to do
        choice = input("\nOptions:\n1. Explore further\n2. Pick up items\n3. Check inventory\nChoose your action (1, 2, or 3): ")

        if choice == "1":
            # Random chance of encountering an enemy while exploring
            if random.choice([True, False]):
                print("Oh no! You encountered an enemy!")
                enemy = random.choice(self.enemies)
                battle(player, enemy)
            else:
                print("You continue exploring.")

        elif choice == "2":
            # Player picks up items in the location
            if self.items:
                player.inventory.extend(self.items)
                self.items = []
                print("You picked up items.")

        elif choice == "3":
            # Display player's inventory
            player.display_inventory()

        else:
            print("Invalid choice. Try again.")

def battle(player, enemy):
    print(f"A wild {enemy} appeared!")

    while player.health > 0 and enemy.health > 0:
        print("\nOptions:")
        print("1. Attack")
        print("2. Use item")
        print("3. Retreat")

        battle_choice = input("Choose your action (1, 2, or 3): ")

        if battle_choice == "1":
            damage_dealt = random.randint(1, 15)
            damage_taken = random.randint(1, 10)
            enemy.health -= damage_dealt
            player.health -= damage_taken

            print(f"\nYou dealt {damage_dealt} damage to the {enemy}.")
            print(f"The {enemy} dealt {damage_taken} damage to you.")

        elif battle_choice == "2":
            if player.inventory:
                item_to_use = random.choice(player.inventory)
                print(f"\nYou used {item_to_use}.")
                player.inventory.remove(item_to_use)
            else:
                print("\nYou don't have any items to use.")

        elif battle_choice == "3":
            print("\nYou chose to retreat. Until next time, adventurer!")
            break

        else:
            print("\nInvalid choice. Try again.")

        print(f"\n{player.name}'s Health: {player.health}")
        print(f"{enemy}'s Health: {enemy.health}")

        if player.health <= 0:
            print("\nGame Over! You were defeated.")
            break
        elif enemy.health <= 0:
            print(f"\nCongratulations! You defeated the {enemy}!")
            break

# Create player
player_name = input("Enter your character's name: ")
player = Player(player_name)

# Create locations
forest = Location("Enchanted Forest", "A mystical forest with magical creatures.", items=["Potion", "Magic Stone"])
cave = Location("Dark Cave", "A pitch-black cave with mysterious sounds echoing.", enemies=["Bat", "Spider"])
village = Location("Peaceful Village", "A small village with friendly inhabitants.", items=["Bread", "Health Elixir"])

# Set initial location
current_location = forest

# Game loop
while player.health > 0:
    current_location.explore(player)

    # Move to a new random location
    locations = [forest, cave, village]
    current_location = random.choice(locations)

print("\nGame Over! Thanks for playing.")
