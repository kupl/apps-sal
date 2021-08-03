from math import log2


def operation(a, b, n=0):
    while log2(a) % 1:
        n += 1
        a //= 2
    return n + abs(log2(a / b))
