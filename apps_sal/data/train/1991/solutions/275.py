from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(source, fuel):
            if fuel < 0:
                return 0

            cnt = 0
            if source == finish:
                cnt += 1
            for i, val in enumerate(locations):
                if i != source:
                    cnt += dfs(i, fuel - abs(locations[source] - val))
            return cnt % mod
        return dfs(start, fuel)
