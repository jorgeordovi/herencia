class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        
    def identificadores(self):
        print(f"Hi I am {self.nombre}")
        
    def mostrar_salud(self):
        print(f"{self.nombre} tiene {self.salud} puntos de salud")