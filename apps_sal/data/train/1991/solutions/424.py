class Solution:

    def countRoutes(self, locations, start, finish, fuel):
        if abs(locations[start] - locations[finish]) > fuel:
            return 0
        l = len(locations)
        dp = [[0 for k in range(fuel + 1)] for j in range(l)]
        dp[start][0] = 1
        for k in range(1, fuel + 1):
            for i in range(l):
                for j in range(l):
                    if i != j:
                        cost = abs(locations[i] - locations[j])
                        if k - cost >= 0:
                            dp[i][k] += dp[j][k - cost]
        ans = 0
        for i in range(fuel + 1):
            ans += dp[finish][i]
        return ans % (10 ** 9 + 7)
