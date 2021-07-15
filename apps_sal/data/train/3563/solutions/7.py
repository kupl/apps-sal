from math import sqrt, floor

def distance(n):
    if n == 1: return 0
    x = floor(sqrt(n-1) + 1) // 2
    return x + abs(x - (n - 4*x*(x + 1) - 1) % (2*x))
