class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        m = len(locations)
        n = fuel+1
        dp = [[0]*n for _ in range(m)]
        dp[start][fuel] = 1
        
        for fuel in reversed(range(1, n)):
            for end in range(m):
                if dp[end][fuel] > 0:
                    for nxt in range(m):
                        cost = abs(locations[end] - locations[nxt])
                        if fuel >= cost and end != nxt:
                            dp[nxt][fuel-cost] += dp[end][fuel]

        return sum(dp[finish]) % (int(1e9) + 7)
