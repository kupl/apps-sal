from functools import lru_cache

def generate_diagonal(nn, l):
    @lru_cache(None)
    def calc(n, ll):
        if n == 0 or ll == 1: return 1
        elif n < 0: return 0
        return calc(n - 1, ll) + calc(n, ll - 1)
    return [calc(nn, i) for i in range(1, l+1)]
