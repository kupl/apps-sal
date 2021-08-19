from math import log10


def rocks(n):
    i = int(log10(n))
    return sum((j * 9 * 10 ** (j - 1) for j in range(1, i + 1))) + (i + 1) * (n - 10 ** i + 1)
