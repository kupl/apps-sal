from math import log2


def operation(a, b):
    c = 0
    while 2 ** int(log2(a)) != a and a > 1:
        a //= 2
        c += 1
    return c + abs(int(log2(b) - log2(a)))
