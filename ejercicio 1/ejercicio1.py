# Version: 1.0
# Fecha: 30/04/2025
# Descripcion: Segmentacion entre pares e impares de una pila de enteros usando una lista enlazada

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None  # Inicia vacía

    # Agrega un elemento
    def push(self, dato):
        try:
            if not isinstance(dato, int):  # Verifica si el dato es un entero
                raise ValueError("El dato debe ser un número entero.")
        except ValueError as e:
            print(e)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope  # El nuevo apunta al anterior tope
        self.tope = nuevo_nodo  # El nuevo nodo ahora es el tope
        print(f"Elemento '{dato}' insertado.")

    # Método que devuelve el elemento del tope sin eliminarlo  
   
    # Método para imprimir los datos de la pila  
    def imprimir(self):  
        if self.tope is None:  
            print("La pila está vacía.")  
        else:  
            print("Contenido de la pila (de arriba hacia abajo):")  
            actual = self.tope  
            while actual is not None:  
                print(actual.dato)  
                actual = actual.siguiente  
    def Mostarordenado(self):
        if self.tope is None:
            print("La pila está vacía.")
            return
        else:
            pares = []
            impares = []
            actual = self.tope  
            while actual is not None:  
                if actual.dato % 2 == 0:  # Si el dato es par
                    pares.append(actual.dato)
                else:  # Si el dato es impar
                    impares.append(actual.dato)
                actual = actual.siguiente    
            print(pares + impares)
            
