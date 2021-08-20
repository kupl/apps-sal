from math import sin, pi


def f(x):
    return sin(x) ** 3 * (3 / 2)


def simpson(n):
    (a, b) = (0, pi)
    h = (b - a) / n
    return h / 3 * (f(a) + f(b) + 4 * sum([f(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1)]) + 2 * sum([f(a + 2 * i * h) for i in range(1, n // 2)]))
