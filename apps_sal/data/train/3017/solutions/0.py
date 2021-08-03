from math import log10


def rocks(n):
    return (n + 1) * int(log10(n) + 1) - (10 ** int(log10(n) + 1) - 1) // 9
