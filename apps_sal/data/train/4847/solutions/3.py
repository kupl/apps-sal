import math

def count_black_cells(h, w):
    return h+w+math.gcd(h,w)-2
