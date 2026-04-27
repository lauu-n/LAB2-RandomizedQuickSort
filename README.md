# LABORATORIO 2: RANDOMIZED QUICK SORT

## Descripción
  Este proyecto presenta un análisis experimental del algoritmo de ordenamiento Randomized Quicksort, evaluando su desempeño en términos de tiempo de ejecución y consumo de memoria.
  El experimento se basa en la ejecución del algoritmo sobre arreglos de diferentes tamaños, realizando múltiples repeticiones para obtener resultados promedio más confiables.

## Metodología
  El experimento se desarrolla de la siguiente manera:
  Se generan arreglos aleatorios sin duplicados.
  Para cada tamaño de entrada:
    - Se ejecuta el algoritmo 100 veces.
    - Para el caso de 10 millones de elementos, se ejecuta 10 veces.
  Se calcula:
    - Tiempo promedio de ejecución.
    - Memoria pico promedio (usando tracemalloc).
  Se generan gráficas para visualizar los resultados.

## Tamaños de entrada
```
  1,000
  5,000
  10,000
  50,000
  100,000
  500,000
  1,000,000
  10,000,000
```

## Resultados
El programa genera:
  - Gráfica de tiempo promedio vs tamaño.
  - Gráfica de memoria pico vs tamaño.
Para observar el comportamiento del algoritmo a medida que crece el tamaño del problema.

## Requisitos
Tener instaladas las siguientes librerías:
```
pip install matplotlib numpy
```

### Integrantes:
  - Carol Arenas
  -Yeimy Beltrán
  - Laura Niño
