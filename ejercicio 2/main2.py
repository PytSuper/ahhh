# Version: 1.0
# Fecha: 30/04/2025
# Descripcion: Hacer un metodo llamado ordenar una pila de enteros de mayor a menor, usando una lista enlazada

# Definición de nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Definición de lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_ordenado(self, valor):
        nuevo = Nodo(valor)
        # Insertar al principio si la lista está vacía o el valor es mayor
        if not self.cabeza or valor > self.cabeza.valor:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.valor > valor:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.valor)
            actual = actual.siguiente
        return resultado

# Función para ordenar una pila usando la lista enlazada
def ordenar_pila(pila):
    lista = ListaEnlazada()
    while pila:
        elemento = pila.pop()
        lista.insertar_ordenado(elemento)
    return lista.a_lista()

