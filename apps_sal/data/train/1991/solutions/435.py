class Solution:

    def countRoutes(
        self, locations: List[int], start: int, finish: int, startFuel: int
    ) -> int:
        MOD = 10 ** 9 + 7
        n = len(locations)

        # (dest index, fuel remaining) -> ways
        dp = [[0 for fuel in range(startFuel + 1)] for dest in range(n)]
        dp[start][startFuel] = 1

        for fuel in reversed(list(range(startFuel))):  # exclude startFuel
            for dest in range(n):
                ways = 0
                for mid in range(n):
                    if mid != dest:
                        d = abs(locations[mid] - locations[dest])
                        if fuel + d <= startFuel:
                            ways += dp[mid][fuel + d]
                dp[dest][fuel] = ways % MOD

        total = 0
        for fuel in range(startFuel + 1):
            total += dp[finish][fuel]
            total %= MOD
        return total
