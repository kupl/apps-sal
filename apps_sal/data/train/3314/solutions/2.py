from math import gcd

def solve(a, b):
    x = gcd(a, b)
    if x == 1: return False
    if x == b: return True
    return solve(a, b//x)
