from collections import defaultdict


class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def f(start, end):
            return abs(locations[start] - locations[end])

        @lru_cache(None)
        def dfs(start, finish, fuel):
            ret = 0
            for i in range(len(locations)):
                if (i == start):
                    continue
                f1 = fuel - f(start, i)
                if f1 >= 0:
                    if i == finish:
                        ret += 1
                    if (f(i, finish) <= f1):
                        ret += dfs(i, finish, f1)
            return ret

        ret = 0
        if (start == finish):
            ret = 1

        ret += dfs(start, finish, fuel)
        return ret % (10**9 + 7)
