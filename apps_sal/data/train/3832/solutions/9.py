import math

def all_permuted(n):
    if n == 0:
        return 1
    
    return n * all_permuted(n - 1) + (-1) ** n
