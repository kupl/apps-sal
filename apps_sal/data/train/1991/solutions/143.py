class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7
        
        def dfs(i, f, dp):
            key = (i,f)
            if key in dp:
                return dp[key]
            ans = 1 if i == finish else 0
            li = locations[i]
            for j, l in enumerate(locations):
                if j == i:
                    continue
                cost = abs(l-li)
                if cost > f:
                    continue
                ans = (ans + dfs(j, f-cost, dp)) % mod
            dp[key] = ans
            return ans
        
        return dfs(start, fuel, {})
