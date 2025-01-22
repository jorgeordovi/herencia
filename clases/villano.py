from clases.personaje import Personaje

class Villano(Personaje):
    def __init__(self, nombre, salud, habilidad):
        super().__init__(nombre, salud)
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"{self.nombre} tiene la habilidad de {self.habilidad}")