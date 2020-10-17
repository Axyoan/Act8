from particula import Particula

class AdministradorParticula:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for p in self.__particulas:
            print(p, '\n')

    def __str__(self):
        ret = ""
        for p in self.__particulas:
            ret += str(p) + '\n'
        return ret