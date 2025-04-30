import main2 as main
print("Ejercicio 2")
print("Ordenar una pila de enteros de mayor a menor usando una lista enlazada")
print("-" * 20)
pila = input("Ingrese los elementos de la pila separados por comas: ")
pila = [int(x) for x in pila.split(",")]
print("Pila original:", pila)
ordenada = main.ordenar_pila(pila)
print("Pila ordenada de mayor a menor:", ordenada)
print("-" * 20)