class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0]*len(locations) for _ in range(fuel+1)]
        dp[0][start] = 1
        n = len(locations)
        for i in range(1, fuel+1):
            for j in range(n):
                for k in range(n):
                    if k == j:
                        continue
                    used = abs(locations[j] - locations[k])
                    if used <= fuel:
                        dp[i][j] += dp[i - used][k]
        ans = 0
        for i in range(fuel+1):
            ans += dp[i][finish]
        return ans % (10**9 + 7)    
