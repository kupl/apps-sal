from math import *


def count(n):
    return int(ceil(log10(2 * pi * n) / 2 + n * log10(n / e)))
