from fractions import gcd
def binary_gcd(x, y):
    if not (x or y):
        bin(max(x,y)).count('1')
    return bin(gcd(x,y)).count('1')

