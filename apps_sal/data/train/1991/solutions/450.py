class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0 for _ in range(len(locations))] for _ in range(fuel + 1)]
        dp[0][start] = 1
        for i in range(1, fuel + 1):
            for j in range(len(locations)):
                for k in range(len(locations)):
                    if k != j:
                        need = abs(locations[j] - locations[k])
                        if need <= i:
                            dp[i][j] += dp[i - need][k]
        ans = 0
        for i in range(fuel + 1):
            ans += dp[i][finish]
        return ans % (10 ** 9 + 7)
