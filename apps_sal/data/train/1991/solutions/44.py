class Solution:
    def countRoutes(self, loc: List[int], s: int, f: int, fuel: int) -> int:
        n = len(loc)

        @lru_cache(None)
        def t(s, f, fuel):

            if fuel < 0:
                return 0

            ct = s == f

            for i in range(n):
                if i != s:
                    ct += t(i, f, fuel - abs(loc[s] - loc[i]))
            return ct

        return t(s, f, fuel) % (10**9 + 7)
