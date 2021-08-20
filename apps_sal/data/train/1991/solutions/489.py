class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def doit(c, fuel):
            tot = 0 if c != finish else 1
            for i in range(len(locations)):
                if i == c:
                    continue
                d = abs(locations[c] - locations[i])
                if d <= fuel:
                    tot += doit(i, fuel - d)
            return tot
        return doit(start, fuel) % (10 ** 9 + 7)
