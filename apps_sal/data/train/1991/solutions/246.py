class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[-1] * (fuel + 1) for i in range(n)]
        mod = 10 ** 9 + 7

        def dfs(cur, fin, fu):
            if fu < 0:
                return 0
            if dp[cur][fu] != -1:
                return dp[cur][fu] % mod
            if cur == fin:
                ans = 1
            else:
                ans = 0
            for i in range(n):
                if i != cur:
                    ans = ans + dfs(i, fin, fu - abs(locations[i] - locations[cur])) % mod
            dp[cur][fu] = ans % mod
            return ans % mod
        return dfs(start, finish, fuel) % mod
