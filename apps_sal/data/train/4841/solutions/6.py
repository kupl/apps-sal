import numpy as np


def simpson(n):
    sum = 0
    h = (np.pi - 0) / n
    for k in range(n + 1):
        x = 0 + k * h
        summand = 1.5 * np.sin(x) ** 3
        if k != 0 and k != n:
            summand *= 2 + 2 * (k % 2)
        sum += summand
    return h / 3 * sum
