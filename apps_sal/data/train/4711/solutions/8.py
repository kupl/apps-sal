from math import log, ceil


def zeros(n):
    return sum((n // 5 ** i for i in range(1, ceil(log(n, 5))))) if n > 0 else 0
