MOD = 10**9+7

class Solution:
    def countRoutes(self, locations, start, finish, fuel):
        dp = [[0 for _ in locations] for _ in range(fuel+1)]
        dp[0][start] = 1
        
        for f in range(fuel+1):
            for i,x in enumerate(locations):
                if abs(x - locations[finish]) > fuel - f:
                    continue
                for j,y in enumerate(locations):
                    if i == j:
                        continue
                    new = f + abs(x-y)
                    if new > fuel:
                        continue
                    dp[new][j] = dp[new][j] + dp[f][i]

        return sum(row[finish] for row in dp) % MOD
