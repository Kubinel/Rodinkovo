import Player
import Enemy
import random

class Main:
    def __init__(self):
        self.player = self.Choose_Character()
        print(f"Welcome {self.player.name} to the game!")

        

        enemy = None
        defeated_enemies = 0
        while True:
            self.player.show_stats() 
            if enemy is None:
                choice = random.randint(1, 4)
                if choice == 1:
                    enemy = Enemy.Zombie()
                elif choice == 2:
                    enemy = Enemy.Skeleton()
                elif choice == 3:
                    enemy = Enemy.Police()
                elif choice == 4:
                    enemy = Enemy.Ork()
        
                print(f"A wild {enemy.name} appears!")
            enemy.show_stats() 
            print()
            self.player.deal_damage(enemy)

            if enemy.hp <= 0:
                print(f"You defeated the {enemy.name}!")
                defeated_enemies += 1
                enemy = None
            else:
                enemy.deal_damage(self.player)
            if self.player.hp <= 0:
                print(f"You were defeated by the {enemy.name}. Game over!")
                print(f"You defeated {defeated_enemies} enemies.")
                break
            
    
    def Choose_Character(self):
        name = input("Enter your name: ")
        print("What character do you want to play as?")
        print("1. Mage")
        print("2. Assasin")
        print("3. Ranger")
        print("4. Warrior")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            return Player.Mage(name)
        elif choice == "2":
            return Player.Assasin(name)
        elif choice == "3":
            return Player.Ranger(name)
        elif choice == "4":
            return Player.Warrior(name)
        
        print("Invalid choice. Defaulting to Mage.")
        return Player.Mage(name)
        

if __name__ == "__main__":
    Main()
