class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def dfs(i, j, f):
            res = 0
            if i == j:
                res += 1
            if f < 0:
                return 0
            for k in range(len(locations)):
                if i == k:
                    continue
                res += dfs(k, j, f - abs(locations[k] - locations[i]))
            return res
        return dfs(start, finish, fuel) % mod
