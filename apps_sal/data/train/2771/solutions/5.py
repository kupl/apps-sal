import sys; sys.setrecursionlimit(10000)
from functools import lru_cache

@lru_cache(maxsize=None)
def Q(n):
    if n <= 2:
        return 1
    return Q(n - Q(n-1)) + Q(n - Q(n-2))
    
def hofstadter_Q(n):
    return Q(n)
