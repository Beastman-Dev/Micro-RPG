# Very basic RPG game

import random
import time
import os

# Functions for pausing the game for a period of time
def pause_global():
    time.sleep(2)
def pause_variable(seconds):
    time.sleep(seconds)

# Function for clearing the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

# Define the creature class
class Creature:
    def __init__(self, name: str, hp: int, attack: int, defense: int) -> None:
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0
        enemy.hp -= damage

    def is_alive(self):
        return self.hp > 0

class Combat:
    def __init__(self, player: Creature, enemies: list) -> None:
        self.player = player
        self.enemies = enemies

    def combat_loop(self):
        round = 1
        x = 0
        
        while True:
            print("\n-------------------------------------------")
            print(f"           ROUND {round}: FIGHT!")
            print("-------------------------------------------")

            # Player turn
            target = self.enemies[x]
            print(f"Player attacks {target.name}!")
            self.player.attack_enemy(target)
            if not target.is_alive():
                print(f"{target.name} has been defeated!")
                x += 1
                print(f"New target: {self.enemies[x].name}")
            else:
                print(f"You attack {target.name} for {self.player.attack - target.defense} damage!")
                print(f"{target.name} has {target.hp} remaining.")
            if not any(enemy.is_alive() for enemy in self.enemies):
                print("You have defeated the enemies!")
                break

            # Enemy turn
            for enemy in self.enemies:
                if enemy.is_alive():
                    enemy.attack_enemy(self.player)
                    if not self.player.is_alive():
                        print("You have died!")

            print(f"Round {round} over!")
            print(f"{self.player.name} HP: {self.player.hp}")
            for enemy in self.enemies:
                if enemy.is_alive():
                    print(f"{enemy.name} HP: {enemy.hp}")

            if not self.player.is_alive():
                break

            round += 1
            pause_global()

# Global variables
player = Creature("Player", 50, 10, 5)
enemies = []
count = 5
for i in range(count):
    enemies.append(Creature(f"Enemy {i + 1}", 25, 8, 2))

# Combat begins
clear_screen()
print("-------------------------------------------")
print("           Combat begins!")
print("-------------------------------------------")
print(f"Player: {player.name}, HP: {player.hp}, Attack: {player.attack}, defense: {player.defense}")
for enemy in enemies:
    print(f"Enemy: {enemy.name}, HP: {enemy.hp}, Attack: {enemy.attack}, defense: {enemy.defense}")

combat = Combat(player, enemies)
combat.combat_loop()
