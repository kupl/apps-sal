import math


def thue_morse(n):
    return morse(2 ** (math.log2(n) // 1 + 1))[0:n]


def morse(m):
    return morse(m / 2) + ''.join([str(int(i) ^ 1) for i in morse(m / 2)]) if m > 1 else '0'
