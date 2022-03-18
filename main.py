from enum import Enum




class Carnivoro:
    def __init__(self) -> None:
        self.tipo = "Carnivoro"


class dieta(Enum):
    herbivoro = Carnivoro().tipo,
    carnivoro = "carnivoro",
    loOtro = "Lo que sea"




class Animal:
    def __init__(self, raza, tipoComida, numero):
        self.id = numero
        self.raza = raza
        self.dieta = dieta[tipoComida].name

class cuidador:
    def __init__(self, nombre, apellido, animales):
        self.nombre = nombre
        self.apellido = apellido
        self.animales = animales

    def getNombre(self):
        print(self.nombre)

class zoo(cuidador):
    pass
        