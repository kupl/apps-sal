class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(i, f):
            if f < 0:
                return 0
            ans = i == finish
            for j in range(n):
                if i != j:
                    ans += dfs(j, f - abs(locations[i] - locations[j]))
            return ans % mod
        return dfs(start, fuel)
