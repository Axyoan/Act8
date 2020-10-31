from particula import Particula
import json


class AdministradorParticula:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula: Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for p in self.__particulas:
            print(p, '\n')

    def __str__(self):
        ret = ""
        for p in self.__particulas:
            ret += str(p) + '\n'
        return ret

    def save_file(self, directory):
        try:
            with open(directory, 'w') as file:
                lista = [particula.to_dict()
                         for particula in self.__particulas]
                json.dump(lista, file, indent=5)
            return 1
        except:
            return 0

    def open_file(self, directory):
        try:
            with open(directory, 'r') as file:
                lista = json.load(file)
                self.__particulas = [Particula(**particula)
                                     for particula in lista]
            return 1
        except:
            return 0

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if(self.cont < len(self.__particulas)):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
