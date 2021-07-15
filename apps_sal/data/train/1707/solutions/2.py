from functools import lru_cache

# Not gonna reinvent the wheel
# Now I can go on codewars while they think I'm still working on it
# Be a smart intern
def cut_log(p, n):
    @lru_cache(maxsize=None)
    def rec(x):
        if not x: return 0
        return max(p[i] + rec(x-i) for i in range(1, x+1))
    return rec(n)
