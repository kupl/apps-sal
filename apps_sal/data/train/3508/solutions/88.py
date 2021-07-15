import math

def halving_sum(n): 
    a = 0
    d = 1
    res = 0
    while a != 1:
        a = math.floor(n / d)
        d *= 2
        res += a
    return res
