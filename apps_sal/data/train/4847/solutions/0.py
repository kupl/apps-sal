from fractions import gcd
def count_black_cells(h, w):
    return (h + w) -2 + gcd(h,w)
