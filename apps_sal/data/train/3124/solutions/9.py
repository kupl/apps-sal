from math import log


def get_exponent(n, p):
    if p <= 1:
        return None
    l, i = None, 0
    while p**i <= abs(n):
        if n % p**i == 0:
            l = i
        i += 1
    return l
