import random

class Player:
    def __init__(self, name, health=100, damage=10):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, enemy):
        damage_dealt = random.randint(1, self.damage)
        enemy.health -= damage_dealt
        return damage_dealt

class Enemy:
    def __init__(self, name, health=50, damage=8):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, player):
        damage_dealt = random.randint(1, self.damage)
        player.health -= damage_dealt
        return damage_dealt

def main():
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    enemy = Enemy("Goblin")

    print(f"Welcome, {player.name}! You encounter a {enemy.name}.")

    while player.health > 0 and enemy.health > 0:
        print("\nOptions:")
        print("1. Attack")
        print("2. Retreat")

        choice = input("Choose your action (1 or 2): ")

        if choice == "1":
            damage_dealt = player.attack(enemy)
            damage_taken = enemy.attack(player)

            print(f"\nYou dealt {damage_dealt} damage to {enemy.name}.")
            print(f"{enemy.name} dealt {damage_taken} damage to you.")

        elif choice == "2":
            print("You chose to retreat. Until next time, adventurer!")
            break

        else:
            print("Invalid choice. Try again.")

        print(f"\n{player.name}'s Health: {player.health}")
        print(f"{enemy.name}'s Health: {enemy.health}")

        if player.health <= 0:
            print("Game Over! You were defeated.")
        elif enemy.health <= 0:
            print(f"Congratulations! You defeated the {enemy.name}!")

if __name__ == "__main__":
    main()
