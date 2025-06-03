class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def deal_damage(self, enemy):
        print(f"{self.name} attacks {enemy.name} for {self.attack} damage!")
        enemy.take_damage(self.attack)

    def take_damage(self, damage):
        damage_taken = damage - self.defense
        if damage_taken < 0:
            damage_taken = 0
        self.hp -= damage_taken
        if self.hp < 0:
            self.hp = 0
            return True
        else:
            return False
        
    def show_stats(self):
        print(f"{self.name} - ❤️  HP: {self.hp} ❤️\t⚔️  Attack: {self.attack} ⚔️\t🛡️  Defense: {self.defense} 🛡️")


## Section for Character classes
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 2000, 50, 5)

    def deal_damage(self, enemy):
        print("Do you want to use fireball (1), freeze (2), magic dust (3) ?")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            damage = self.attack
            print(f"You used fireball for {damage} damage!")
        if choice == "2":
            damage = self.attack + 20
            print(f"You used freeze for {damage} damage!")
        if choice == "3":
            damage = self.attack + 50
            print(f"You used magic dust for {damage} damage!")
        enemy.take_damage(damage)
        

class Assasin(Character):
    def __init__(self, name):
        super().__init__(name, 3500, 40, 3)

    def deal_damage(self, enemy):
        print("Do you want to use dagger (1), dagger rush (2), back stab (3) ?")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            damage = self.attack
            print(f"You used dagger for {damage} damage!")
        if choice == "2":
            damage = self.attack + 20
            print(f"You used dagger rush for {damage} damage!")
        if choice == "3":
            damage = self.attack + 50
            print(f"You used magic back stab for {damage} damage!")
        enemy.take_damage(damage)


# TODO: Implement the Ranger and Warrior classes with unique abilities
class Ranger(Character):
    def __init__(self, name):
        super().__init__(name, 3000, 30, 4)

    def deal_damage(self, enemy):
        print("Do you want to use fireball (1), freeze (2), magic dust (3) ?")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            damage = self.attack
            print(f"You used fireball for {damage} damage!")
        if choice == "2":
            damage = self.attack + 20
            print(f"You used freeze for {damage} damage!")
        if choice == "3":
            damage = self.attack + 50
            print(f"You used magic dust for {damage} damage!")
        enemy.take_damage(damage)

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 4000, 20, 10)

    def deal_damage(self, enemy):
        print("Do you want to use fireball (1), freeze (2), magic dust (3) ?")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            damage = self.attack
            print(f"You used fireball for {damage} damage!")
        if choice == "2":
            damage = self.attack + 20
            print(f"You used freeze for {damage} damage!")
        if choice == "3":
            damage = self.attack + 50
            print(f"You used magic dust for {damage} damage!")
        enemy.take_damage(damage)

