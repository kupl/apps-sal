from math import ceil, log10


def cycle(d):
    if d % 5 == 0 or d % 2 == 0:
        return -1
    n = 10 ** int(ceil(log10(d)))
    first = n % d
    n *= 10
    for i in range(99999999):
        n %= d
        if n == first:
            return i + 1
        n *= 10
