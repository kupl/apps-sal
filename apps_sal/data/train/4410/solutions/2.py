from math import log10, floor, log


def count_sixes(n):
    k = floor(log10(3) + (n - 1) * log10(2))
    return k - (k * log(10) > (n - (n & 1)) * log(2))
