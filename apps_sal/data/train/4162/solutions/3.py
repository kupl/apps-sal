from math import log2

def friends(n):
    return int(log2(max(2, n) - 1))
