# i0 = 0.14849853757254047
from math import e
def weight(n, w):
    total = 1
    for i in range(1, n + 1): 
        total += e ** (-2 * i)
    return w * 0.14849853757254047 * total

