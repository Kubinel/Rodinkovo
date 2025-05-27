import Player
import Enemy
import random

class Main:
    def __init__(self):
        name = input("Enter your name: ")
        print("What character do you want to play as?")
        print("1. Mage")
        print("2. Assasin")
        print("3. Ranger")
        print("4. Warrior")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            self.player = Player.Mage(name)
        elif choice == "2":
            self.player = Player.Assasin(name)
        elif choice == "3":
            self.player = Player.Ranger(name)
        elif choice == "4":
            self.player = Player.Warrior(name)
        else:
            print("Invalid choice. Defaulting to Mage.")
            self.player = Player.Mage(name)

        while True:
            choice = random.randint(1, 4)
            if choice == 1:
                enemy = Enemy.Zombie()
            elif choice == 2:
                enemy = Enemy.Skeleton()
            elif choice == 3:
                enemy = Enemy.Police()
            elif choice == 4:
                enemy = Enemy.Ork()
        

if __name__ == "__main__":
    Main()
