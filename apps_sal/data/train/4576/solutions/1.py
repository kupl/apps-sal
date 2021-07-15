from fractions import gcd

def gcd_matrix(a, b):
    return round(sum(gcd(x, y) for x in a for y in b) / (len(a) * len(b)), 3)

