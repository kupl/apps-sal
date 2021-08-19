from math import sin
from math import pi


def f(x):
    return 3 / 2 * sin(x) ** 3


def simpson(n):
    return pi / (3 * n) * (f(0) + f(pi) + 4 * sum((f((2 * i - 1) * (pi / n)) for i in range(1, n // 2 + 1))) + 2 * sum((f(2 * i * (pi / n)) for i in range(1, n // 2))))
