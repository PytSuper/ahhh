# Version 1.0
# Integrantes: Elian Olivares, Camilo Galeano, Enrique Solis, Joshua Vilchez
# Fecha: 28/04/2025
# Descripción: Este programa permite gestionar una ruta de estaciones,
# donde se pueden agregar estaciones y calcular el tiempo estimado entre dos estaciones.

from ruta import Ruta

def main():
    ruta = Ruta()

    # Carga de estaciones
    print("Carga de estaciones (deja el nombre vacío para terminar)")
    while True:
        nombre = input("Nombre de la estación: ")
        if nombre == "":
            break
        try:
            tiempo = int(input("Tiempo hasta la siguiente estación (en minutos): "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue
        ruta.agregar_estacion(nombre, tiempo)

    ruta.mostrar_ruta()

    # Consulta dinámica del tiempo
    while True:
        print("Consultar tiempo estimado (deja vacío para salir)")
        inicio = input("Estación de inicio: ")
        if inicio == "":
            break
        destino = input("Estación de destino: ")
        if destino == "":
            break

        tiempo = ruta.calcular_tiempo(inicio, destino)
        if tiempo is not None:
            print(f"Tiempo estimado de {inicio} a {destino}: {tiempo} minutos\n")
        else:
            print("Ruta no válida o estaciones no encontradas.\n")

if __name__ == "__main__":
    main()
