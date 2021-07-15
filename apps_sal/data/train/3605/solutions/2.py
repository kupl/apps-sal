from operator import mul
from functools import reduce

def choose(n, p):
    if (p > n - p):
        p = n - p
    return reduce(mul, list(range((n-p+1), n+1)), 1) // reduce( mul, list(range(1,p+1)), 1)
        
def diagonal(n, p):
    return choose(n+1, p+1)

