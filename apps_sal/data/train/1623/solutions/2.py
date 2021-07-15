import math
from fractions import Fraction
from functools import lru_cache

#cache = {}
@lru_cache(maxsize = 10000)
def bernoulli_number(n):
    #if n in cache: return cache[n]
    if (n == 0): return 1
    if (n == 1): return Fraction(-1,2)
    if (n%2 != 0): return 0
    res = 0
    
    for j in range(n):
        res += -Fraction(1,(n+1)) * Fraction(math.factorial(n+1),math.factorial(j)*math.factorial(n+1-j)) * bernoulli_number(j) 
    
    #cache[n] = res
    return res

