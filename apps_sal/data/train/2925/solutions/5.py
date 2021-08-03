from math import log10


def multiply(n):
    return n * 5**int(log10(abs(n)) + 1) if n != 0 else 0
