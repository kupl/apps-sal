class Solution:

    def countRoutes(self, loc: List[int], start: int, finish: int, fuel: int) -> int:

        @functools.lru_cache(None)
        def helper(i, f):
            if i == finish:
                return 1 + sum((helper(j, f - abs(loc[i] - loc[j])) for j in range(len(loc)) if j != i and f >= abs(loc[i] - loc[j])))
            return sum((helper(j, f - abs(loc[i] - loc[j])) for j in range(len(loc)) if j != i and f >= abs(loc[i] - loc[j])))
        return helper(start, fuel) % (10 ** 9 + 7)
