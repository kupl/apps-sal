class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        \"\"\"
        how many routes arrived at city c, with fuel f
        
        dp[c][f]
        for prev in range(n):
            if f+ gas <= fuel:
                dp[c][f] += dp[prev][f+gas] 
        init: dp[start][fuel] = 1
        return sum(dp[finish][any])
        \"\"\"
        n = len(locations)
        M = 10 ** 9 + 7
        dp = [[0] * (201) for _ in range(n)] 
        dp[start][fuel] = 1
        for f in range(fuel, -1, -1):
            for c in range(n):
                for prev in range(n):
                    if prev == c: continue
                    gas = abs(locations[prev] - locations[c])
                    if f+gas <= fuel:
                        dp[c][f] = (dp[c][f] + dp[prev][f+gas]) % M
        total = 0
        for f in range(fuel+1):
            total += dp[finish][f]
        return total % M
