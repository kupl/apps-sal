from math import log

def zeros(n):
    if n == 0:
        return 0
    z = 0
    k = 1
    kMax = round(log(n, 5))
    for i in range(k, kMax+1):
        z += n // (5 ** i)
    return z
