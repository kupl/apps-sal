class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # dp[i][j] = number of ways to get to location j from starting position using exact i amount of fuels  
        n = len(locations)
        dp = [[0 for i in range(n)] for j in range(fuel + 1)]
        dp[0][start] = 1
        
        for i in range(1, fuel + 1):
            for j in range(n):
                # we need an intermediate location k, such that start ---->k and k -----j
                # we enumerate all possible locations k
                for k in range(n):
                    if j != k:
                        need_fuel = abs(locations[k] - locations[j])
                        if i >= need_fuel:
                            dp[i][j] += dp[i - need_fuel][k]
                        
        
        ans = 0
        for f in range(fuel + 1):
            ans += dp[f][finish]
            
        return ans % (10**9 + 7)
