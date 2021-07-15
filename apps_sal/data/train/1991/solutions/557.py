class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10 ** 9 + 7
        @lru_cache(None)
        def dfs(i, f):
            if f < 0:
                return 0
            res = int(i == finish)
            for j in range(n):
                if j != i:
                    dist = abs(locations[i] - locations[j])
                    if dist <= f:
                        res = (res + dfs(j, f - dist)) % mod
            return res
        
        return dfs(start, fuel)

