class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        (now, target) = (locations[start], locations[finish])

        @functools.lru_cache(None)
        def helper(now, fuel):
            if abs(now - target) > fuel:
                return 0
            ret = 1 if now == target else 0
            for l in locations:
                if l == now:
                    continue
                cost = abs(l - now)
                if fuel >= cost:
                    ret += helper(l, fuel - cost)
            return ret
        return helper(now, fuel) % (10 ** 9 + 7)
