import math


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def find_bounds(n):
    low_prod = 0
    high_prod = 0
    low = 0
    high = 0
    for x in range(1, n + 1):
        low = high
        low_prod = high_prod
        high += find(x)
        high_prod += x * find(x)
        if high_prod > n:
            ratio = (n - low_prod) / (high_prod - low_prod)
            return (ratio, high, low)


@memoize
def find(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    (ratio, high, low) = find_bounds(n)
    return low + math.ceil((high - low) * ratio)
