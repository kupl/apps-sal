class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        DP = [[-1 for _ in range(fuel + 1)] for _ in range(N)]

        def dp(i, k):
            if k < 0:
                return 0
            if DP[i][k] >= 0:
                return DP[i][k]
            ans = 1 if i == finish else 0
            for j in range(N):
                if i == j:
                    continue
                ans += dp(j, k - abs(locations[i] - locations[j]))
            ans %= 1000000007
            DP[i][k] = ans
            return ans
        return dp(start, fuel)
