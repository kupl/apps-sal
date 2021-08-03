\"\"\"
dp[f][c]: when arriving at city c, with fuel f left

for d in range(n):
    gas = abs(locations[d] - locations[c])
    dp[f][c] += dp[f+gas][d]
    
return sum(dp[f][finish]) for all f
    
\"\"\"



class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0 for i in range(101)] for j in range(201)]
        mod = 10 ** 9 + 7
        n = len(locations)
        dp[fuel][start] = 1
        
        
        for f in range(fuel, -1, -1):
            for c in range(n):
                for d in range(n):
                    if d == c:
                        continue
                    gas = abs(locations[d] - locations[c])
                    if f + gas <= fuel:
                        dp[f][c] = (dp[f][c] + dp[f+gas][d]) % mod
        
        res = 0
        for f in range(fuel+1):
            res = (res + dp[f][finish]) % mod
        return res
        
        
        
        
        
        
        
        
        
