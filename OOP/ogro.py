from enemigo import *

class ogro(enemigo):
    def __int__(self, puntos_energia=10, ataque=1):
        super().__init__(tipo_enemigo='ogro', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("Ogro aplasta todo!!*")
