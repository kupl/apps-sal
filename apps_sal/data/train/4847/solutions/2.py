from math import gcd
def count_black_cells(h, w):
    return h + w + gcd(h, w) - 2
