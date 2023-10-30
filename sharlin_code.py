import json
import math
import matplotlib.pyplot as plt

# Leer los archivos JSON
with open('Filter_Etiqueta_B10_03_3_1_Bright Field_004.json', 'r') as file1, open('shar.json', 'r') as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

# Calcular la métrica de coincidencia (distancia euclidiana en este caso)
def euclidean_distance(circle1, circle2):
    x1, y1 = circle1['x'], circle1['y']
    x2, y2 = circle2['x'], circle2['y']
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

coincidencia_total = 0
for circle1 in data1['frame'][0]['circle']:
    for circle2 in data2['frame'][0]['circle']:
        distancia = euclidean_distance(circle1, circle2)
        coincidencia_total += 1 / (1 + distancia) # Cuanto más cerca, mayor coincidencia

# Mostrar resultados matemáticamente
print("Nivel de coincidencia:", coincidencia_total)

# Mostrar resultados gráficamente
for circle1 in data1['frame'][0]['circle']:
    plt.scatter(circle1['x'], circle1['y'], c='red', label='Archivo 1', s=50)
for circle2 in data2['frame'][0]['circle']:
    plt.scatter(circle2['x'], circle2['y'], c='blue', label='Archivo 2', s=50)
plt.legend()
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Nivel de Coincidencia de Coordenadas')
plt.show()