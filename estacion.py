# Esta modulo define la clase Estacion, que representa una estación en la ruta.
class Estacion:
    def __init__(self, nombre, tiempo_siguiente):
        self.nombre = nombre
        self.tiempo_siguiente = tiempo_siguiente
        self.siguiente = None