import numpy as np
import math


def f(x):
    return 3 / 2 * np.power(math.sin(x), 3)


def simpson(n: int):
    (a, b) = (0, np.pi)
    h = (b - a) / n
    (suma1, suma2) = (0, 0)
    for i in range(1, n // 2 + 1):
        suma1 = suma1 + f(a + (2 * i - 1) * h)
    for i in range(1, n // 2):
        suma2 = suma2 + f(a + 2 * i * h)
    calka = h / 3 * (f(a) + f(b) + 4 * suma1 + 2 * suma2)
    return calka
