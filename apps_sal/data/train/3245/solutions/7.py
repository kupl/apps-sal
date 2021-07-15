from operator import mul
from functools import reduce

def choose(n, p):
    if (p > n): 
        return 0
    if (p > n - p): 
        p = n - p
    return reduce(mul, range((n-p+1), n+1), 1) // reduce( mul, range(1,p+1), 1)

def checkchoose(m, n):
    mx = choose(n, n // 2)
    if (m > mx): 
        return -1
    i = 0
    while (i <= (n // 2) + 1):
        if choose(n, i) == m:
            return i
        i += 1
    return -1
