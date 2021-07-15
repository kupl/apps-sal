import sys

sys.setrecursionlimit(1200)

cache = {}

def number_of_routes(m, n):
    if m == 0 or n == 0: return 1
    if m > n: return number_of_routes(n, m)
    result = cache.get((m,n))
    if result is None:
        cache[m,n] = result = number_of_routes(m-1, n) + number_of_routes(m, n-1)
    return result
