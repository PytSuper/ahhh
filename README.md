# Gestión de Ruta de Estaciones

**Versión:** 1.0
**Fecha:** 28/04/2025

## Integrantes

* Elian Olivares
* Camilo Galeano
* Enrique Solis
* Joshua Vilchez

## Descripción

Este programa permite gestionar una ruta de estaciones de transporte utilizando una lista enlazada. El programa realiza las siguientes funciones:

1.  **Carga de Estaciones:**
    *   Permite al usuario ingresar el nombre de cada estación y el tiempo (en minutos) hasta la siguiente estación.
    *   Las estaciones se agregan a una ruta (implementada como una lista enlazada).
    *   El proceso de carga termina cuando el usuario ingresa un nombre de estación vacío.
    *   Valida que el tiempo ingresado sea un número entero.

2.  **Mostrar Ruta:**
    *   Una vez cargadas las estaciones, el programa muestra la ruta completa con los tiempos entre estaciones consecutivas.

3.  **Consulta de Tiempo Estimado:**
    *   Permite al usuario consultar el tiempo estimado de viaje entre dos estaciones específicas (inicio y destino).
    *   El usuario ingresa los nombres de las estaciones de inicio y destino.
    *   El proceso de consulta termina si el usuario deja vacío el nombre de la estación de inicio o destino.
    *   Calcula y muestra el tiempo total si la ruta es válida (la estación de destino está después de la de inicio y ambas existen en la ruta).
    *   Muestra un mensaje de error si la ruta no es válida o las estaciones no se encuentran.

## Cómo Ejecutar

1.  Asegúrate de tener Python instalado.
2.  Guarda los archivos `estacion.py`, `ruta.py` y `f.py` en el mismo directorio.
3.  Abre una terminal o línea de comandos en ese directorio.
4.  Ejecuta el programa principal con el comando: `python f.py`
5.  Sigue las instrucciones en pantalla para cargar las estaciones y consultar los tiempos.
