import tkinter as tk
from Casti import Casti

class Kreslic:
    def __init__(self, slovo):
        self.root = tk.Tk()
        self.root.title("Kreslic")
        self.canvas = tk.Canvas(self.root, width=500, height=600, bg="white")
        self.canvas.pack()

        self.slovo = slovo
        self.pouzite_pismenka = []
        self.chyby = 0

        self.casti = Casti(self.canvas, slovo)
        self.casti.nakresli_sibenicu()
        self.policka = self.casti.nakresli_policka()

        self.txt = tk.Text(self.root, height=1, width=10)
        self.txt.pack()
        self.btn = tk.Button(self.root, text="Hadaj", command=self.vyhodnot)
        self.btn.pack()
        
        
        
        
        
        self.root.mainloop()

    def vyhodnot(self):
        self.canvas.delete("hodnotenie")
        hadane = self.txt.get("1.0", "end-1c").lower()
        if len(hadane) > 1:
            self.canvas.create_text(250, 550, text="Zadaj len jedno písmeno!", fill="red", tag="hodnotenie")
            return
        else:
            if hadane in self.pouzite_pismenka:
                self.canvas.create_text(250, 550, text="Toto písmeno si už použil!", fill="red", tag="hodnotenie")
                return
            else:
                self.pouzite_pismenka.append(hadane)
                for pismeno in self.slovo:
                    if hadane == pismeno:
                        index = self.slovo.index(pismeno)
                        coords = self.canvas.coords(self.policka[index])
                        self.canvas.delete(self.policka[index])
                        self.canvas.create_text(coords[0]+5, coords[1], text=pismeno, fill="black")