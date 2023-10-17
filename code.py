"""Definiciones de funciones de centroides_a_arreglo().

Se trata de un programa que contiene las funciones del Proyecto
Eléctrico.
"""


def centroides_a_arreglo(json):
    """
    Función que toma archivo .json y retorna arreglo.

    Función para obtener centroides de archivo .json y colocarlos todos
    en un arreglo


    """
    # Se crea arreglo vacío para guardar los valores "x" y "y".
    xy_valores = []

    # Se itera sobre los datos del archivo .json y se extraen
    # los valores "x" y "y".
    for frame in json["frame"]:
        for circle in frame["circle"]:
            x_value = circle["x"]
            y_value = circle["y"]
            xy_valores.append((x_value, y_value))

        return xy_valores


"""

from sklearn.cluster import DBSCAN
import numpy as np

# Función para agrupar coordenadas similares y asignar etiquetas
def clusterizar_coordenadas(coordenadas, epsilon, min_muestras):
    # Convierte las coordenadas a un arreglo NumPy
    datos = np.array(coordenadas)

    # Inicializa y ajusta el modelo de agrupamiento DBSCAN
    dbscan = DBSCAN(eps=epsilon, min_samples=min_muestras)
    etiquetas = dbscan.fit_predict(datos)

    return etiquetas

# Ejemplo de conjuntos de datos (sustituye estos con tus propias coordenadas)
conjunto1 = [(1, 2), (3, 4), (5, 6), (10, 10)]
conjunto2 = [(2, 3), (4, 5), (5, 6), (12, 11)]

# Establece los parámetros de DBSCAN (puedes necesitar ajustarlos)
# epsilon = 1.0  # Distancia máxima entre dos muestras para ser consideradas 
# parte del mismo grupo
min_muestras = 2  # Número mínimo de muestras en un grupo

# Agrupa las coordenadas
etiquetas1 = clusterizar_coordenadas(conjunto1, epsilon, min_muestras)
etiquetas2 = clusterizar_coordenadas(conjunto2, epsilon, min_muestras)

# Compara las etiquetas para determinar la similitud
def comparar_etiquetas(etiquetas1, etiquetas2):
    similitud = 0
    for etiqueta1 in set(etiquetas1):
        for etiqueta2 in set(etiquetas2):
            if np.array_equal(np.where(etiquetas1 == etiqueta1), np.where(etiquetas2 == etiqueta2)):
                similitud += 1

    return similitud

similitud = comparar_etiquetas(etiquetas1, etiquetas2)

print(f"Similitud entre los dos conjuntos de datos: {similitud}")

"""
