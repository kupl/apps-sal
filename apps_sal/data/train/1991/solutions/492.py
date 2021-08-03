class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0 for j in range(fuel + 1)] for k in range(n)]
        dp[start][fuel] = 1

        for k in range(fuel, -1, -1):
            for j in range(n):

                for i in range(n):
                    if i == j:
                        continue
                    dist = abs(locations[i] - locations[j])
                    if (fuel - k) >= dist:
                        dp[j][k] += dp[i][k + dist]
        res = 0
        for k in range(fuel + 1):
            res += dp[finish][k]
        mod = 1000000007
        # print(res)
        return res % mod
