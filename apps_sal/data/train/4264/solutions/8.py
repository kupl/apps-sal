from math import log2


def operation(a,b):
    i = 0
    while log2(a) != int(log2(a)):
        a //= 2
        i += 1
    return i  + abs(log2(a) - log2(b))
