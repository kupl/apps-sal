from math import log2


def operation(a, b):
    return abs(log2(a) - log2(b)) if log2(a).is_integer() else 1 + operation(a // 2, b)
