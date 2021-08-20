from functools import lru_cache


def least_bribes(bribes):

    @lru_cache(maxsize=10000)
    def _rec(lst):
        if len(lst) <= 2:
            return sum(lst)
        return min((max(_rec(lst[:i]), _rec(lst[i + 1:])) + lst[i] for i in range(1, len(lst) - 1)))
    return _rec(tuple(bribes))
