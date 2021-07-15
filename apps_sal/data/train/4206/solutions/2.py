from math import log2

def three_details(n):
    i = int(log2(n))
    return min(abs(n - 2**p) for p in (i, i + 1))
