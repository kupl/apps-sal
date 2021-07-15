from math import log2

def t(n):
    if n == 0:
        return 0
    k = int(log2(n))
    i = n - 2**k
    if i == 0:
        return (2**(2*k+1)+1) // 3
    else:
        return t(2**k) + 2*t(i) + t(i+1) - 1

toothpick = t
