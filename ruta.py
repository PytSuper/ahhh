# Este modulo define la clase Ruta, y contiene métodos para agregar estaciones, 
# mostrar la ruta y calcular el tiempo entre dos estaciones.
from estacion import Estacion

class Ruta:
    def __init__(self):
        self.inicio = None

    # Se crea una nueva estación y se añade al final de la lista enlazada
    def agregar_estacion(self, nombre, tiempo_siguiente):
        nueva = Estacion(nombre, tiempo_siguiente)
        if not self.inicio:
            self.inicio = nueva
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva

    
    # Se recorre la lista enlazada y se imprime el nombre de cada estación
    def mostrar_ruta(self):
        actual = self.inicio
        print("\nRuta actual:")
        while actual:
            print(f"{actual.nombre}", end=" -> ")
            actual = actual.siguiente
        print("Fin\n")

    # Se recorre la lista enlazada desde la estación de inicio hasta la estación de destino
    def calcular_tiempo(self, inicio_nombre, destino_nombre):
        actual = self.inicio
        tiempo_total = 0
        en_ruta = False

        while actual:
            if actual.nombre == inicio_nombre:
                en_ruta = True

            if en_ruta:
                if actual.nombre == destino_nombre:
                    return tiempo_total
                tiempo_total += actual.tiempo_siguiente

            actual = actual.siguiente

        return None
