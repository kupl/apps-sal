class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0] * n for _ in range(fuel + 1)] 
        dp[fuel][start] = 1
        M = int(1e9+7)
                
        for f in range(fuel, 0, -1):
            for i in range(n):
                for j in range(i + 1, n):
                    dis = abs(locations[i] - locations[j])
                    if dis <= f:
                        dp[f - dis][j] = (dp[f - dis][j] + dp[f][i]) % M
                        dp[f - dis][i] = (dp[f - dis][i] + dp[f][j]) % M
        ans = 0
        for f in range(fuel + 1):
            ans += dp[f][finish]
        return ans % M
