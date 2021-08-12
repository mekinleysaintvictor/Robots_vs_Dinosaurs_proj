from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.name = "Dinosaur Fleet"
        self.dinos = []

    def add_dinos(self):
        first_dino = Dinosaur("Frank")
        second_dino = Dinosaur("Samantha")
        third_dino = Dinosaur("Viola")
        self.dinos.append(first_dino)
        self.dinos.append(second_dino)
        self.dinos.append(third_dino)