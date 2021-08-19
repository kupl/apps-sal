import math


def count_sixes(n):
    n0 = int(math.log10(2) * (n - 1))
    n1 = int(math.log10(2) * n)
    n2 = int(math.log10(2) * (n + 1))
    len = n1
    if n1 == n2 and n1 == n0 + 1 and (n % 2 != 0):
        len = n0
    return len
