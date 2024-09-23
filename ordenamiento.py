import time
import random
import string
import matplotlib.pyplot as plt

# 1. Implementación de Algoritmos de Ordenamiento

def ordenamiento_burbuja(lista):
    """
    Ordenamiento por Burbuja.
    Recorre repetidamente la lista, comparando elementos adyacentes y
    permutándolos si están en el orden incorrecto.
    """
    n = len(lista)
    lista = lista.copy()  # Crear una copia para no modificar la original
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenamiento_seleccion(lista):
    """
    Ordenamiento por Selección.
    Divide la lista en una parte ordenada y otra desordenada, seleccionando
    el elemento mínimo de la parte desordenada y colocándolo al final de la parte ordenada.
    """
    n = len(lista)
    lista = lista.copy()
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def ordenamiento_insercion(lista):
    """
    Ordenamiento por Inserción.
    Construye la lista ordenada una elemento a la vez, tomando cada elemento
    y colocándolo en la posición correcta dentro de la parte ya ordenada.
    """
    lista = lista.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def ordenamiento_rapido(lista):
    """
    Ordenamiento Rápido (QuickSort).
    Selecciona un pivote y particiona la lista en elementos menores y mayores al pivote,
    aplicando recursivamente el mismo proceso a las sublistas.
    """
    if len(lista) <= 1:
        return lista.copy()
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return ordenamiento_rapido(menores) + [pivote] + ordenamiento_rapido(mayores)

def ordenamiento_fusion(lista):
    """
    Ordenamiento por Fusión (MergeSort).
    Divide la lista en mitades, las ordena recursivamente y luego fusiona las listas ordenadas.
    """
    if len(lista) <= 1:
        return lista.copy()

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mitad = len(lista) // 2
    izquierda = ordenamiento_fusion(lista[:mitad])
    derecha = ordenamiento_fusion(lista[mitad:])

    return merge(izquierda, derecha)

# 2. Pruebas y Comparación

# Generar conjuntos de datos de prueba
def generar_cadenas(n):
    """Genera una lista de n cadenas aleatorias."""
    return [''.join(random.choices(string.ascii_letters, k=5)) for _ in range(n)]

listas_prueba = {
    "Enteros Pequeños": [64, 34, 25, 12, 22, 11, 90],
    "Decimales": [0.5, 2.3, 0.1, 9.8, 4.4],
    "Cadenas": ['z', 'y', 'a', 'b', 'x'],
    "Lista Grande Descendente": list(range(1000, 0, -1)),
    "Lista Grande Ascendente": list(range(1000)),
    "Lista Grande Aleatoria": random.sample(range(1, 10001), 1000),
    "Cadenas Grandes": generar_cadenas(1000)
}

# Definir los algoritmos a evaluar
algoritmos = {
    "Burbuja": ordenamiento_burbuja,
    "Selección": ordenamiento_seleccion,
    "Inserción": ordenamiento_insercion,
    "QuickSort": ordenamiento_rapido,
    "MergeSort": ordenamiento_fusion
}

# Función para medir el tiempo de ejecución
def medir_tiempo(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista)
    fin = time.time()
    return fin - inicio

# Almacenar los tiempos de ejecución
resultados = {alg: [] for alg in algoritmos.keys()}
tamanos = []

# Evaluar cada algoritmo con cada lista de prueba
for nombre_lista, lista in listas_prueba.items():
    tamaño = len(lista)
    tamanos.append(tamaño)
    print(f"Evaluando {nombre_lista} (Tamaño: {tamaño})")
    for nombre_alg, alg_func in algoritmos.items():
        tiempo = medir_tiempo(alg_func, lista)
        resultados[nombre_alg].append(tiempo)
        print(f"  {nombre_alg}: {tiempo:.6f} segundos")
    print("-" * 50)

# 3. Visualización de Resultados

# Filtrar solo las listas grandes para una gráfica más clara
filtro = ["Lista Grande Descendente", "Lista Grande Ascendente", "Lista Grande Aleatoria", "Cadenas Grandes"]
tamanos_filtrados = [len(listas_prueba[n]) for n in filtro]

plt.figure(figsize=(12, 8))
for nombre_alg, tiempos in resultados.items():
    tiempos_filtrados = [resultados[nombre_alg][i] for i, n in enumerate(listas_prueba.keys()) if n in filtro]
    plt.plot(tamanos_filtrados, tiempos_filtrados, marker='o', label=nombre_alg)

plt.title('Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento')
plt.xlabel('Tamaño de la Lista')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.show()

# 4. Análisis de Resultados

# Nota: El análisis se debe realizar manualmente basado en los resultados obtenidos.
# Sin embargo, aquí se proporciona una impresión resumida.

print("\nAnálisis de Resultados:")
for nombre_alg, tiempos in resultados.items():
    promedio = sum(tiempos) / len(tiempos)
    print(f"  {nombre_alg}: Tiempo promedio = {promedio:.6f} segundos")

print("\nObservaciones:")
print("""
- **Burbuja, Selección e Inserción:** Tienen una complejidad temporal de O(n²), lo que los hace ineficientes para listas grandes. Esto se refleja en tiempos de ejecución significativamente mayores en listas de tamaño 1000.
- **QuickSort y MergeSort:** Ambos tienen una complejidad temporal de O(n log n), lo que los hace mucho más eficientes para listas grandes. QuickSort suele ser más rápido en la práctica debido a menores constantes, pero MergeSort garantiza estabilidad y rendimiento consistente.
- **QuickSort:** Puede tener un rendimiento variable dependiendo de la elección del pivote, pero en general es muy eficiente.
- **MergeSort:** Utiliza más memoria adicional debido a la necesidad de fusionar sublistas, pero es muy estable y eficiente para grandes conjuntos de datos.
- **Listas de Cadenas:** Los algoritmos muestran patrones similares, pero el tiempo puede variar ligeramente debido a la comparación de cadenas en lugar de números.
""")

# 5. Ventajas y Desventajas de los Algoritmos

print("\nVentajas y Desventajas de los Algoritmos:")

tabla = """
| Algoritmo        | Ventajas                                                | Desventajas                                           |
|------------------|---------------------------------------------------------|-------------------------------------------------------|
| Burbuja          | Fácil de implementar                                    | Muy ineficiente para listas grandes                   |
| Selección        | Fácil de entender y codificar                           | Ineficiente para grandes conjuntos de datos           |
| Inserción        | Eficiente en listas casi ordenadas                      | Desempeño deficiente con listas largas y desordenadas |
| QuickSort        | Muy eficiente en la mayoría de los casos                | Puede ser ineficiente en listas ya ordenadas          |
| MergeSort        | Estable y garantiza O(n log n)                          | Usa más memoria debido a la división de listas        |
"""

print(tabla)