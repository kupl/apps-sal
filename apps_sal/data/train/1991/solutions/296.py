class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # dp[i][f] = # of ways to reach city i (from start) with fuel f left.
        n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]
        dp[start][fuel] = 1  # init

        # State transition: dp[i][f] = sum{dp[j][f + d]} where d = abs(location[i]-location[j]), i != j
        for f in range(fuel, 0, -1):
            for i in range(0, n):
                if dp[i][f] == 0:
                    continue
                for j in range(0, n):
                    d = abs(locations[i] - locations[j])
                    if i == j or d == 0 or d > f:
                        continue
                    dp[j][f - d] = (dp[j][f - d] + dp[i][f]) % 1_000_000_007

        return sum(dp[finish]) % 1_000_000_007
