class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10 ** 9 + 7
        dp = [[-1] * (fuel + 1) for _ in range(n)]

        def dfs(s, remain):
            if remain < 0:
                return 0
            if dp[s][remain] != -1:
                return dp[s][remain]
            res = 0
            if s == finish:
                res += 1
            for i in range(n):
                if i != s:
                    res += dfs(i, remain - abs(locations[i] - locations[s]))
            dp[s][remain] = res
            return res
        return dfs(start, fuel) % mod
