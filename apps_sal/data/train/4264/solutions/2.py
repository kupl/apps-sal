from math import log2


def operation(a, b):
    if log2(a).is_integer():
        return abs(log2(a) - log2(b))
    return 1 + operation(a // 2, b)
