class Casti:
    def __init__(self, canvas, slovo):
        self.canvas = canvas
        self.slovo = slovo

    def nakresli_sibenicu(self):
        self.canvas.create_rectangle(0,0, 500, 400, fill = "lightblue")
        self.canvas.create_rectangle(0,380, 500, 410, fill = "green")
        self.canvas.create_rectangle(20,20, 50, 400, fill="black")
        self.canvas.create_rectangle(20,20, 300, 50, fill="black")
        self.canvas.create_rectangle(250,50, 251, 100, fill="black")
        print("Nakresli sibenicu")


    def nakresli_policka(self):
        policka = []
        offset = 600 - (len(self.slovo)+2) * 50
        for i in range(len(self.slovo)):
            x1 = offset / 2 + 10 +(i * 50)
            x2 = x1 + 20
            policko = self.canvas.create_rectangle(x1,500,x2,501)
            policka.append(policko)
        return policka