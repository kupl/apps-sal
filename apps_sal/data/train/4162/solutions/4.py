from math import log2

def friends(n):
    return int(log2(n-1)) if n>1 else 0
