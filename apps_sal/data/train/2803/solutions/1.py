from fractions import gcd


def DPC_sequence(s):
    n = 1
    for (i, c) in enumerate(s, 1):
        if c == 'D':
            n = n * i // gcd(n, i)
    for (i, c) in enumerate(s, 1):
        g = gcd(n, i)
        if c == 'P' and 1 < g:
            return -1
        if c == 'C' and (not 1 < g < i):
            return -1
    return n
