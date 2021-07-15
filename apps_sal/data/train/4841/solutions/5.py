import math


def f(x):
    return 3 / 2 * math.sin(x) ** 3


def simpson(n):
    h = math.pi / n
    a = 0
    res = f(0) + f(math.pi)
    for i in range(1, n // 2 + 1):
        res += 4 * f((2 * i - 1) * h)
    for i in range(1, n // 2):
        res += 2 * f(2 * i * h)
    res *= math.pi / (3 * n)
    return res
