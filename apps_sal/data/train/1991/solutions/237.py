class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dfs(current, fuel):
            ans = 0
            if fuel >= 0:
                if current == finish:
                    ans += 1
                for (i, loc) in enumerate(locations):
                    if i != current:
                        consume = abs(locations[current] - loc)
                        ans += dfs(i, fuel - consume)
            return ans % (10 ** 9 + 7)
        ret = dfs(start, fuel)
        return ret
