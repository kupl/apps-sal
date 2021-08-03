import sys
sys.setrecursionlimit(1500)


def padovan(n, memo={0: 1, 1: 1, 2: 1}):
    if n in memo:
        return memo[n]
    else:
        result = padovan(n - 2, memo) + padovan(n - 3, memo)
        memo[n] = result
        return result
