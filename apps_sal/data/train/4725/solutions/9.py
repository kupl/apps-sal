from math import log10


def reverse(n):
    l = int(log10(n))
    return sum((n // 10 ** i % 10 * 10 ** (l - i) for i in range(l + 1)))
