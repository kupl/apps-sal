class Solution:
    def countRoutes(self, a: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 + 7
        ans = 0
        start = a[start]
        finish = a[finish]

        @lru_cache(None)
        def solve(c, f):
            if f < 0:
                return 0
            ans = 0
            if c == finish:
                ans += 1
            for x in a:
                if x == c:
                    continue
                ans += solve(x, f - abs(x - c))
            return ans % mod

        return solve(start, fuel)
