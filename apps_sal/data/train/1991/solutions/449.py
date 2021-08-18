class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(cur, end, fuel):
            if fuel == 0:
                return cur == end
            ret = cur == end
            for l in locations:
                if l == cur:
                    continue
                if abs(l - cur) <= fuel:
                    ret += dfs(l, end, fuel - abs(l - cur))
            return ret
        return dfs(locations[start], locations[finish], fuel) % (10 ** 9 + 7)
