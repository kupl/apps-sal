from functools import lru_cache

@lru_cache(maxsize=None)
def factor_sum(n):
    i, res, save = 2, 0, n
    while i*i <= n:
        while not n%i:
            n, res = n//i, res+i
        i += 1 + i%2 # 2 -> 3 -> 5 -> 7 -> ...
    if n > 2: res += n
    return res if res == save else factor_sum(res)
