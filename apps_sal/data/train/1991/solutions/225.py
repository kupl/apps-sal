from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        s, f = locations[start], locations[finish]
        locations.sort()

        maps = {}
        for i, loc in enumerate(locations):
            maps[loc] = i

        @lru_cache(maxsize=None)
        def helper(l, r, fuel):
            if l == r:
                count = 1
                for loc in locations:
                    if loc != l and abs(loc - l) + abs(loc - r) <= fuel:
                        n1 = 1
                        n2 = helper(loc, r, fuel - abs(loc - l))
                        count += n2
                return count
            if abs(r - l) > fuel:
                return 0
            else:
                count = 0
                for loc in locations:
                    if loc != l and abs(loc - l) + abs(loc - r) <= fuel:
                        n1 = 1
                        n2 = helper(loc, r, fuel - abs(loc - l))
                        count += n2
                return count

        return helper(s, f, fuel) % (10 ** 9 + 7)
