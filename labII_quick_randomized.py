"""
Randomized Quicksort - Análisis de Tiempo de Ejecución
=======================================================
- 100 experimentos por tamaño (promedio) excepto 10M → 10 experimentos
- Usa tracemalloc para monitorear memoria
- Genera gráficas de tiempo vs tamaño de entrada
"""

import time
import random
import tracemalloc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


# ──────────────────────────────────────────────
# 1. IMPLEMENTACIÓN DE RANDOMIZED QUICKSORT
def randomized_partition(arr, low, high):
    # Elige pivote aleatorio y hace la partición.
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]  # mueve pivote al final
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr, low, high):
    # Quicksort con pivote aleatorio (in-place, iterativo para evitar recursión profunda).
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = randomized_partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))


# ──────────────────────────────────────────────
# 2. FUNCIÓN DE EXPERIMENTO
def run_experiment(n, num_experiments):
    """
    Ejecuta `num_experiments` veces el 
    Randomized Quicksort sobre arreglos 
    de tamaño n y devuelve:
    - tiempo promedio (segundos)
    - memoria pico promedio (KB)
    """
    times = []
    memories = []
    for _ in range(num_experiments):
        arr = random.sample(range(n * 10), n)   # arreglo aleatorio sin duplicados
        tracemalloc.start()
        t_start = time.perf_counter()
        randomized_quicksort(arr, 0, n - 1)
        t_end = time.perf_counter()
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append(t_end - t_start)
        memories.append(peak / 1024)   # bytes → KB
    return np.mean(times), np.mean(memories)


# ──────────────────────────────────────────────
# 3. CONFIGURACIÓN DE EXPERIMENTOS
sizes = [1_000, 5_000, 10_000, 50_000, 100_000, 500_000, 1_000_000]
EXPERIMENTS_DEFAULT = 100
print("=" * 55)
print("  Randomized Quicksort — Análisis de Tiempo")
print("=" * 55)
print(f"{'Tamaño (n)':>12}  {'Experimentos':>12}  {'Tiempo (s)':>12}  {'Mem. pico (KB)':>15}")
print("-" * 55)

avg_times   = []
avg_memories = []

for n in sizes:
    num_exp = EXPERIMENTS_DEFAULT
    avg_t, avg_mem = run_experiment(n, num_exp)
    avg_times.append(avg_t)
    avg_memories.append(avg_mem)
    print(f"{n:>12,}  {num_exp:>12}  {avg_t:>12.6f}  {avg_mem:>15.2f}")

print("=" * 55)


# ──────────────────────────────────────────────
# 4. GRÁFICAS
BG      = "#0f0f1a"
ACCENT  = "#7ef9c0"
ACCENT2 = "#f97ef6"
GRID    = "#ffffff15"
TEXT    = "#e8e8f0"

plt.rcParams.update({
    "figure.facecolor":  BG,
    "axes.facecolor":    BG,
    "axes.edgecolor":    "#444466",
    "axes.labelcolor":   TEXT,
    "xtick.color":       TEXT,
    "ytick.color":       TEXT,
    "text.color":        TEXT,
    "grid.color":        GRID,
    "grid.linestyle":    "--",
    "font.family":       "monospace",
    "font.size":         10,
})

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Randomized Quicksort — Análisis de Rendimiento",
            fontsize=14, fontweight="bold", color=ACCENT, y=1.01)

x_labels = [f"{n:,}" for n in sizes]
x_pos    = np.arange(len(sizes))

# ── Gráfica 1: Tiempo promedio ──
ax1 = axes[0]
ax1.plot(x_pos, avg_times, color=ACCENT, linewidth=2.5,
        marker="o", markersize=7, markerfacecolor=BG, markeredgewidth=2)
ax1.fill_between(x_pos, avg_times, alpha=0.15, color=ACCENT)
ax1.set_title("Tiempo promedio de ejecución", color=TEXT, pad=10)
ax1.set_xlabel("Tamaño del arreglo (n)")
ax1.set_ylabel("Tiempo promedio (segundos)")
ax1.set_xticks(x_pos)
ax1.set_xticklabels(x_labels, rotation=40, ha="right", fontsize=8)
ax1.grid(True)

# Anotación del mayor valor
max_t_idx = np.argmax(avg_times)
ax1.annotate(f"{avg_times[max_t_idx]:.3f}s",
            xy=(x_pos[max_t_idx], avg_times[max_t_idx]),
            xytext=(-40, 12), textcoords="offset points",
            color=ACCENT, fontsize=9,
            arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.2))

# ── Gráfica 2: Memoria pico promedio ──
ax2 = axes[1]
ax2.plot(x_pos, avg_memories, color=ACCENT2, linewidth=2.5,
        marker="s", markersize=7, markerfacecolor=BG, markeredgewidth=2)
ax2.fill_between(x_pos, avg_memories, alpha=0.15, color=ACCENT2)
ax2.set_title("Memoria pico promedio (tracemalloc)", color=TEXT, pad=10)
ax2.set_xlabel("Tamaño del arreglo (n)")
ax2.set_ylabel("Memoria pico promedio (KB)")
ax2.set_xticks(x_pos)
ax2.set_xticklabels(x_labels, rotation=40, ha="right", fontsize=8)
ax2.grid(True)

max_m_idx = np.argmax(avg_memories)
ax2.annotate(f"{avg_memories[max_m_idx]:.0f} KB",
            xy=(x_pos[max_m_idx], avg_memories[max_m_idx]),
            xytext=(-50, 12), textcoords="offset points",
            color=ACCENT2, fontsize=9,
            arrowprops=dict(arrowstyle="->", color=ACCENT2, lw=1.2))

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/quicksort_rendimiento.png",
            dpi=150, bbox_inches="tight", facecolor=BG)
print("\n✓ Gráfica guardada: quicksort_rendimiento.png")
