from estacion import Estacion

class Ruta:
    def __init__(self):
        self.inicio = None

    def agregar_estacion(self, nombre, tiempo_siguiente):
        nueva = Estacion(nombre, tiempo_siguiente)
        if not self.inicio:
            self.inicio = nueva
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva

    def mostrar_ruta(self):
        actual = self.inicio
        print("\nRuta actual:")
        while actual:
            print(f"{actual.nombre}", end=" -> ")
            actual = actual.siguiente
        print("Fin\n")

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
