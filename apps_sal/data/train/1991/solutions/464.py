class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if abs(locations[finish] - locations[start]) > fuel:
            return 0
        M = 1000000007
        n = len(locations)
        dp = [[0] * n for i in range(fuel + 1)]
        for i in range(fuel + 1):
            dp[i][finish] = 1
        for f in range(1, fuel + 1):
            for s in range(n):
                for s1 in range(n):
                    if s == s1:
                        continue
                    if abs(locations[s1] - locations[s]) <= f:
                        dp[f][s] = (dp[f][s] + dp[f - abs(locations[s] - locations[s1])][s1]) % M
        return dp[fuel][start]
