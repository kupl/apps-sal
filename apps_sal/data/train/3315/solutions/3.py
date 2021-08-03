from math import log2


def strongest_even(n, m):
    b = x = 2**int(log2(m))

    while not n <= x <= m:
        b //= 2
        x = (m // b) * b

    return x
