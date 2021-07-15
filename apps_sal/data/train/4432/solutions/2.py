from functools import lru_cache

def can_jump(arr):
    @lru_cache(maxsize=None)
    def rec(i):
        if i >= len(arr)-1: return i >= len(arr)
        return any(rec(i+j) for j in range(1, arr[i]+1))
    return rec(0)
