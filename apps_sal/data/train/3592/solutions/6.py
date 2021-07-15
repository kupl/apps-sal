from math import gcd, ceil

def lcm(x, y):
    return x * y // gcd(x, y)

def greatest(x, y, n):
    m = lcm(x, y)
    p = n // m - (not n % m)
    return p * m
    
def smallest(x, y, n):
    m = lcm(x, y)
    p = n // m + 1
    return p * m
