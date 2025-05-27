from Player import Character

class Zombie(Character):
    def __init__(self):
        super().__init__("Zombie", 100, 18, 2)

class Skeleton(Character):
    def __init__(self):
        super().__init__("Skeleton", 60, 30, 0)

class Police(Character):
    def __init__(self):
        super().__init__("Police", 40, 60, 3)

class Ork(Character):
    def __init__(self):
        super().__init__("Ork", 150, 12, 10)

class Cyclops(Character):
    def __init__(self):
        super().__init__("Cyclops", 250, 10, 0)

class Vampire(Character):
    def __init__(self):
        super().__init__("Vampire", 130, 33, 5)


