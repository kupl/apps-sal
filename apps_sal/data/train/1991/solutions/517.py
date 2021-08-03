class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7
        l = len(locations)
        dp = [[0] * l for i in range(fuel + 1)]
        dp[fuel][start] = 1
        for f in range(fuel, 0, -1):
            for a in range(l):
                for b in range(l):
                    dist = abs(locations[a] - locations[b])
                    if a != b and f >= dist:
                        dp[f - dist][b] += dp[f][a]
                        if dp[f - dist][b] > mod:
                            dp[f - dist][b] %= mod
        ans = 0
        for i in range(fuel + 1):
            ans += dp[i][finish]
            ans %= mod
        return ans
