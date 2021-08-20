from functools import lru_cache


class Solution:

    def countRoutes(self, loc: List[int], start: int, finish: int, fuel: int) -> int:
        l = len(loc)
        MAX = 10 ** 9 + 7

        @lru_cache(None)
        def inner(curr, lf):
            if curr == finish and lf == 0:
                return 1
            if lf <= 0:
                return 0
            ans = int(curr == finish)
            for i in range(l):
                if i == curr:
                    continue
                ans += inner(i, lf - abs(loc[i] - loc[curr]))
            return ans % MAX
        return inner(start, fuel)
