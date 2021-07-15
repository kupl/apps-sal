class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        memo = {}
        def dfs(u, fuel):
            if (u, fuel) in memo:
                return memo[u, fuel]
            ans = 1 if u == finish else 0
            for v in range(len(locations)):
                cost = abs(locations[u] - locations[v])
                if cost > 0 and cost <= fuel:
                    ans += dfs(v, fuel - cost)
            ans %= 1000000007
            memo[u, fuel] = ans
            return ans
        
        return dfs(start, fuel)
