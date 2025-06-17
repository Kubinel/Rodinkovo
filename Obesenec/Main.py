from Kreslic import Kreslic
from random import choice

class Main:
    def __init__(self):
        slova = ["policajt", "python", "programko", "obesenec", "slovo", "hokej", "futbal", "roblox", "poki", "minecraft"]
        slovo = choice(slova)
        self.kreslic = Kreslic(slovo)
    

if __name__ == "__main__":
    Main()
    