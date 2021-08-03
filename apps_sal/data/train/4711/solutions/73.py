from math import log


def zeros(n):
    if n == 0:
        return 0
    z = 0
    i = 1
    while i < log(n, 5):
        z += n // 5**i
        i += 1

    return z
