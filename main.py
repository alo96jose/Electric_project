import json
import code

# Se abre el archivo .json
with open("B10_03_3_1_Bright Field_004.json", "r") as f:
    # Cargar los datos del archivo .json a un objeto de Python
    datos = json.load(f)

arreglo = centroides_a_arreglo(datos)

# Imprimir los datos
#print(datos)
