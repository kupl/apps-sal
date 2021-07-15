from operator import mul
from functools import reduce

def choose(n, p):
    if (p > n): return 0
    if (p > n - p): p = n - p
    return reduce(mul, range((n-p+1), n+1), 1) // reduce( mul, range(1,p+1), 1)
def number_of_routes(m, n):
    return choose(m + n, n)
