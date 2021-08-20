import math


def suma(i):
    return sum((x ** 2 + (i // x) ** 2 for x in range(1, math.ceil(i ** 0.5)) if not i % x)) + (i if (i ** 0.5).is_integer() else 0)


def list_squared(m, n):
    return [[i, suma(i)] for i in range(m, n + 1) if (suma(i) ** 0.5).is_integer()]
