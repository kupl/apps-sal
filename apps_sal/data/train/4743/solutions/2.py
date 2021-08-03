from functools import lru_cache


def target_game(values):
    @lru_cache(maxsize=None)
    def rec(i):
        if i >= len(values):
            return 0
        if values[i] <= 0:
            return rec(i + 1)
        return max(rec(i + 1), values[i] + rec(i + 2))
    return rec(0)
