class Solution:
    def countRoutes(self, loc: List[int], start: int, finish: int, fuel: int) -> int:

        if abs(loc[start] - loc[finish]) > fuel:
            return 0

        s, f = loc[start], loc[finish]
        loc = sorted(loc)

        start, end = loc.index(s), loc.index(f)
        if start > end:
            start, end = end, start

        @lru_cache(None)
        def dp(i, gas):
            if gas < 0:
                return 0

            ans = 0
            if i == end:
                ans += 1

            for nxt in range(len(loc)):
                if nxt != i:
                    ans += dp(nxt, gas - abs(loc[i] - loc[nxt]))

            return ans

        res = dp(start, fuel)

        return res % (10**9 + 7)
