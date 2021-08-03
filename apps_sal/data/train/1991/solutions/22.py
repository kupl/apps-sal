from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(maxsize=None)
        def dfs(idx, f):
            cur = 0
            if f < 0:
                return cur
            if idx == finish:
                cur += 1
            for i in range(len(locations)):
                if i != idx:
                    cur += dfs(i, f - abs(locations[i] - locations[idx]))
            return cur

        return dfs(start, fuel) % (10 ** 9 + 7)
