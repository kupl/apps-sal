from functools import lru_cache


@lru_cache(maxsize=None)
def rec(n): return 1 + (0 if n == 1 else rec(3 * n + 1) if n & 1 else rec(n // 2))


memo = [[0, None], [1, 1]]


def max_collatz_length(n):
    if not (type(n) == int and n > 0):
        return []
    while n >= len(memo):
        x = rec(len(memo))
        if x > memo[-1][1]:
            memo.append([len(memo), x])
        else:
            memo.append(memo[-1])
    return memo[n]
