import tkinter as tk
from Casti import Casti

class Kreslic:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kreslic")
        self.canvas = tk.Canvas(self.root, width=500, height=600, bg="white")
        self.canvas.pack()

        self.casti = Casti(self.canvas, "policajt")
        self.casti.nakresli_sibenicu()
        
        
        
        
        
        self.root.mainloop()