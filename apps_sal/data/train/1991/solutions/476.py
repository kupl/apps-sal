class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 1000000007
        dp = [[0 for i in range(fuel + 1)] for j in range(len(locations))]
        r = len(locations)
        c = len(locations)
        ans = 0
        dp[start][0] = 1
        dp[start][fuel] = 1
        for fue in range(1, fuel + 1):
            for i in range(r):
                for j in range(r):
                    if j == i:
                        continue
                    need = abs(locations[i] - locations[j])
                    if need <= fue:
                        dp[i][fue] = (dp[i][fue] + dp[j][fue - need]) % MOD
            ans += dp[finish][fue]
        print(dp)
        return ans % MOD
