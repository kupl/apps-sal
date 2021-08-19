class Solution:

    def countRoutes(self, a: List[int], s: int, e: int, fuel: int) -> int:
        n = len(a)
        mod = 10 ** 9 + 7
        memo = {}

        def dp(u, f):
            if f < 0:
                return 0
            if (u, f) in memo:
                return memo[u, f]
            ans = 0
            if u == e:
                ans += 1
            for v in range(n):
                if v != u:
                    ans += dp(v, f - abs(a[u] - a[v]))
                    ans %= mod
            memo[u, f] = ans
            return ans
        return dp(s, fuel)
