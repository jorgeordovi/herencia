from clases.heroe import Heroe
from clases.villano import Villano


superman = Heroe("Superman", 100, "volar")
joker = Villano("Joker", 80, "Robar Bancos") # Prmera escena de batman

####
superman.identificadores()
superman.mostrar_salud()

superman.mostrar_poder()

joker.identificadores()
joker.mostrar_salud()

joker.mostrar_habilidad()