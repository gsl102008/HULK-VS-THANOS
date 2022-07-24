import random

class player:
    def __init__(self, name, position, hp, damage):
        self.name = name
        self.position = position
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0
    
    def attack(self, other):
        other.hp -= self.damage
        print(f"{self.name} attacks {other.name} for {self.damage} damage.")

    def __str__(self):
        return f"{self.name} is a {self.position} with {self.hp} health and does {self.damage} damage."


class game:
    def __init__(self):
        self.player1 = player("Player 1", "HULK", 100, 20)
        self.player2 = player("Player 2", "THANOS", 80, 30)

    def turn(self):
        while True:
            if not self.player1.is_alive():
                print("Player 2 wins!")
                return

            if not self.player2.is_alive():
                print("Player 1 wins!")
                return

            print(f"\n{self.player1}\n{self.player2}\n")

            choice = input("Who will you attack? (HULK or THANOS)\n")

            if choice == "HULK":
                attacker, defender = self.player1, self.player2
            elif choice == "THANOS":
                attacker, defender = self.player2, self.player1

            attacker.attack(defender)

    def __str__(self):
        return f"\n{self.player1}\n{self.player2}\n"



g = game()
g.turn()