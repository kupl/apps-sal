import math


def weight(n, w):
    x0 = math.exp(-1)
    i0 = 0.14849853757254047
    p = i0
    for i in range(1, n+1):
        x = math.exp(-i-1)
        k = x/x0
        p += i0*k*k
    return p*w
