\"\"\"
dp[f][c]: when arriving at city c, with fuel f left

for d in range(n):
    gas = abs(locations[d] - locations[c])
    dp[f][c] += dp[f+gas][d]
    
return sum(dp[f][finish]) for all f


dp[f][3] <- dp[f+1][2], dp[f+2][1], dp[f+3][0]


0 1 2 3

dp[f][c][k] k=0: stay, k=1: moving right, k=2: moving left

for f in range(fuel, -1, -1):
    for c in range(n):
        if c>0:
            gas = lications[c] - locations[c-1]
            dp[f][c][0] += dp[f+gas][c-1][1] + dp[f+gas][c-1][0]
            dp[f][c][1] += dp[f+gas][c-1][1] + dp[f+gas][c-1][0]
        if c < n-1:
            gas = lications[c+1] - locations[c-1]
            dp[f][c][0] += dp[f+gas][c+1][2] + dp[f+gas][c+1][0]
            dp[f][c][2] += dp[f+gas][c+1][2] + dp[f+gas][c+1][0]
            
return sum{dp[f][finish][0]} for all f

\"\"\"



class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[[0 for i in range(3)] for j in range(201)] for _ in range(201)]
        mod = 10 ** 9 + 7
        startPos = locations[start]
        finishPos = locations[finish]
        locations.sort()
        n = len(locations)
        
        startIdx, finishIdx = 0, 0
        for i in range(n):
            if locations[i]==startPos:
                startIdx = i
            if locations[i]==finishPos:
                finishIdx = i
        
        dp[fuel][startIdx][0] = 1
        
        for f in range(fuel, -1, -1):
            for c in range(n):
                if c>0 and f+locations[c]-locations[c-1] <= fuel:
                    gas = locations[c] - locations[c-1]
                    dp[f][c][0] += dp[f+gas][c-1][1] + dp[f+gas][c-1][0]
                    dp[f][c][1] += dp[f+gas][c-1][1] + dp[f+gas][c-1][0]
                if c < n-1 and f+locations[c+1]-locations[c] <= fuel:
                    gas = locations[c+1] - locations[c]
                    dp[f][c][0] += dp[f+gas][c+1][2] + dp[f+gas][c+1][0]
                    dp[f][c][2] += dp[f+gas][c+1][2] + dp[f+gas][c+1][0]
        
        dp[f][c][0] %= mod
        dp[f][c][1] %= mod
        dp[f][c][2] %= mod
                
        res = 0
        for f in range(fuel+1):
            res = (res + dp[f][finishIdx][0]) % mod
        return res
        
        
        
        
        
        
        
