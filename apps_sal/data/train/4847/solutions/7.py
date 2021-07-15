from math import gcd

def count_black_cells(h, w):
    return w + h + gcd(h, w) - 2
