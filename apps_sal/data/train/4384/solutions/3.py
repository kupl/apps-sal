from fractions import gcd

def fraction(a, b):
    d = gcd(a, b)
    return a//d + b//d
