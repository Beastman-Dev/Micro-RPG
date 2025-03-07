# Very basic RPG game

import random
import time

# Define the creature class
class Creature:
    def __init__(self, name: str, hp: int, attack: int, defence: int) -> None:
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defence
        if damage < 0:
            damage = 0
        enemy.hp -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage!\n")
        time.sleep(2)

    def is_alive(self):
        return self.hp > 0

def pause():
    time.sleep(3)

# Variables
player = Creature("Player", 100, 10, 5)
enemy_1 = Creature("Enemy 1", 50, 8, 2)
enemy_2 = Creature("Enemy 2", 50, 8, 2)
round = 1

# Combat begins
print("-------------------------------------------")
print("           Combat begins!")
print("-------------------------------------------")
pause()
print(f"Player: {player.name}, HP: {player.hp}, Attack: {player.attack}, Defence: {player.defence}")
pause()
print(f"Enemy: {enemy_1.name}, HP: {enemy_1.hp}, Attack: {enemy_1.attack}, Defence: {enemy_1.defence}")
pause()
print(f"Enemy: {enemy_2.name}, HP: {enemy_2.hp}, Attack: {enemy_2.attack}, Defence: {enemy_2.defence}")
pause()
print("\n-------------------------------------------")
print(f"           ROUND {round}: FIGHT!")
print("-------------------------------------------")
pause()
while True:
    if enemy_1.is_alive():
        player.attack_enemy(enemy_1)
        enemy_1.attack_enemy(player)
        enemy_2.attack_enemy(player) 
    elif enemy_2.is_alive():
        player.attack_enemy(enemy_2)
        enemy_2.attack_enemy(player)
    else:
        print("You have won!")
        break
    if not player.is_alive():
        print("You have died!")
        break
    print(f"Round {round} over!")
    time.sleep(3)
    print(f"{player.name} HP: {player.hp}")
    if enemy_1.is_alive():
        print(f"{enemy_1.name} HP: {enemy_1.hp}")
    if enemy_2.is_alive():
        print(f"{enemy_2.name} HP: {enemy_2.hp}")
    print("\n")
    round += 1
    time.sleep(3)