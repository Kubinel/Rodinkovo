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


## Section for Character classes
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 2000, 50, 5)
 
class Assasin(Character):
    def __init__(self, name):
        super().__init__(name, 3500, 40, 3)

class Ranger(Character):
    def __init__(self, name):
        super().__init__(name, 3000, 30, 4)

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 4000, 20, 10)

