from math import *
import numpy as np
from decimal import *


def f(xk, yk):
    return 2 - exp(-4 * xk) - 2 * yk


def Y(t):
    return 1 + 0.5 * exp(-4 * t) - 0.5 * exp(-2 * t)


def ex_euler(n):
    x = 0
    y0 = 1
    T = 1
    h = 1 / n
    y = np.zeros(n + 1)
    z = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + f(x, y[i]) * h
        z[i] = Y(x)
        x += h
    z[len(z) - 1] = Y(x)
    A = [abs(y[i] - z[i]) / z[i] for i in range(n + 1)]
    return round(1e-06 * trunc(1000000.0 * np.mean(A, dtype=np.float32)), 6)
