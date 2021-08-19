class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def helper(loc, fuel):
            if loc == finish and fuel == 0:
                return 1
            elif loc != finish and fuel == 0:
                return 0
            s = 0
            if loc == finish:
                s = 1
            for i in range(length):
                if i == loc:
                    continue
                dist = abs(locations[i] - locations[loc])
                if dist <= fuel:
                    s = (s + helper(i, fuel - dist)) % MOD
            return s
        MOD = 10 ** 9 + 7
        length = len(locations)
        return helper(start, fuel)
