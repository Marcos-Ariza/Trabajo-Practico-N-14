# **Comparación de Algoritmos de Ordenamiento en Python**

Este proyecto implementa y compara cinco algoritmos clásicos de ordenamiento: Burbuja, Selección, Inserción, QuickSort y MergeSort. El objetivo es evaluar el rendimiento de cada uno en diferentes tipos de conjuntos de datos, midiendo los tiempos de ejecución y visualizando los resultados mediante gráficos.

## **Tabla de Contenidos**
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Algoritmos Implementados](#algoritmos-implementados)
3. [Conjuntos de Datos](#conjuntos-de-datos)
4. [Requisitos Previos](#requisitos-previos)
5. [Instrucciones de Instalación](#instrucciones-de-instalación)
6. [Ejecución del Proyecto](#ejecución-del-proyecto)
7. [Visualización de Resultados](#visualización-de-resultados)
8. [Análisis](#análisis)
9. [Ventajas y Desventajas de los Algoritmos](#ventajas-y-desventajas-de-los-algoritmos)
10. [Licencia](#licencia)

## **Descripción del Proyecto**
Este proyecto tiene como propósito comparar el rendimiento de los algoritmos de ordenamiento más comunes, implementados en Python, utilizando distintos conjuntos de datos. Se miden los tiempos de ejecución de cada algoritmo y se presentan gráficamente para analizar su eficiencia en diferentes escenarios.

Los algoritmos de ordenamiento son:
- Burbuja
- Selección
- Inserción
- QuickSort
- MergeSort

El código genera gráficos que ilustran la diferencia de rendimiento entre estos algoritmos cuando se aplican a diferentes tamaños y tipos de listas.

## **Algoritmos Implementados**
1. **Ordenamiento Burbuja (Bubble Sort):** Comparación y permutación de elementos adyacentes en la lista. Complejidad: `O(n²)`.
2. **Ordenamiento Selección (Selection Sort):** Selecciona el menor elemento en la lista y lo coloca en su posición final. Complejidad: `O(n²)`.
3. **Ordenamiento Inserción (Insertion Sort):** Inserta cada elemento en su lugar dentro de la parte ya ordenada de la lista. Complejidad: `O(n²)`.
4. **QuickSort:** Selecciona un pivote, particiona la lista en elementos menores y mayores al pivote y los ordena recursivamente. Complejidad promedio: `O(n log n)`.
5. **MergeSort:** Divide la lista en mitades, ordena las mitades y las combina. Complejidad: `O(n log n)`.

## **Conjuntos de Datos**
El proyecto evalúa los algoritmos con diferentes tipos de listas:
- **Enteros Pequeños:** Una lista de enteros aleatorios con tamaño pequeño.
- **Decimales:** Lista de números decimales.
- **Cadenas:** Lista de caracteres o cadenas de texto.
- **Lista Grande Descendente:** Enteros en orden descendente.
- **Lista Grande Ascendente:** Enteros en orden ascendente.
- **Lista Grande Aleatoria:** Lista aleatoria de enteros.
- **Cadenas Grandes:** Lista de cadenas aleatorias generadas dinámicamente.

El tamaño de las listas varía entre pequeños conjuntos (por ejemplo, 7 elementos) y listas más grandes (1000 elementos).

## **Requisitos Previos**
Antes de ejecutar el proyecto, asegúrate de que tu entorno cumple con los siguientes requisitos:
- Python 3.6 o superior
- Bibliotecas:
  - `matplotlib` para visualización de gráficos.

Puedes instalar `matplotlib` usando el siguiente comando:
```bash
pip install matplotlib
```

## **Instrucciones de Instalación**
1. Clona este repositorio en tu máquina local o descarga el archivo.
    ```bash
    git clone https://github.com/tu_usuario/nombre_repositorio.git
    ```
2. Accede al directorio del proyecto:
    ```bash
    cd nombre_repositorio
    ```

3. Instala las dependencias necesarias ejecutando el siguiente comando:
    ```bash
    pip install -r requirements.txt
    ```

> **Nota:** Si no tienes un archivo `requirements.txt`, instala solo `matplotlib` como se indicó previamente.

## **Ejecución del Proyecto**
Para ejecutar el código, sigue estos pasos:

1. Asegúrate de estar en el directorio del proyecto.
2. Ejecuta el script principal:
    ```bash
    python ordenamiento.py
    ```

El código realizará las siguientes acciones:
- Implementará cada uno de los algoritmos de ordenamiento en diferentes conjuntos de datos.
- Medirá los tiempos de ejecución de cada algoritmo.
- Generará un gráfico que compara los tiempos de ejecución según el tamaño de la lista.
- Mostrará un análisis y observaciones en la consola.

## **Visualización de Resultados**
Una vez que ejecutes el script, verás gráficos que muestran el rendimiento de los algoritmos. Los ejes del gráfico son:

- **Eje X:** Tamaño de las listas de prueba.
- **Eje Y:** Tiempo de ejecución en segundos.

Cada línea del gráfico representa uno de los algoritmos de ordenamiento, permitiéndote visualizar cómo cambia el rendimiento a medida que el tamaño de la lista aumenta.

## **Análisis**
Al finalizar la ejecución del script, se imprime un análisis general de los tiempos promedio de cada algoritmo. Este análisis permite observar patrones de eficiencia y establecer cuál es el mejor algoritmo para distintos tamaños y tipos de listas.

Observaciones típicas incluyen:
- **Burbuja, Selección e Inserción:** Algoritmos ineficientes para listas grandes, con complejidad de `O(n²)`.
- **QuickSort y MergeSort:** Mucho más eficientes, con una complejidad de `O(n log n)`, siendo ideales para listas grandes.

## **Ventajas y Desventajas de los Algoritmos**

| Algoritmo        | Ventajas                                                | Desventajas                                           |
|------------------|---------------------------------------------------------|-------------------------------------------------------|
| Burbuja          | Fácil de implementar                                    | Muy ineficiente para listas grandes                   |
| Selección        | Fácil de entender y codificar                           | Ineficiente para grandes conjuntos de datos           |
| Inserción        | Eficiente en listas casi ordenadas                      | Desempeño deficiente con listas largas y desordenadas |
| QuickSort        | Muy eficiente en la mayoría de los casos                | Puede ser ineficiente en listas ya ordenadas          |
| MergeSort        | Estable y garantiza O(n log n)                          | Usa más memoria debido a la división de listas        |
