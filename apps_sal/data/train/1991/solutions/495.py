class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = []
        n = len(locations)
        for i in range(fuel + 1):
            dp.append([0] * n)
        dp[0][finish] = 1
        for i in range(1, fuel + 1):
            for j in range(n):
                ways = 0
                if j == finish:
                    ways += 1
                for k in range(n):
                    if k != j and abs(locations[k] - locations[j]) <= i:
                        fuel_remain = i - abs(locations[k] - locations[j])
                        ways += dp[fuel_remain][k]
                dp[i][j] = ways
        return dp[fuel][start] % (10 ** 9 + 7)
