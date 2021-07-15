from math import ceil

def branch(n):
    if n == 1:
        return 0
    l = int(ceil(n ** 0.5)) // 2
    n -= (2 * l - 1) ** 2 + 1
    return n // (2*l or 1)
