import functools


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        @functools.lru_cache(None)
        def foo(loc, f):
            res = 1 if loc == finish else 0
            for i in range(len(locations)):
                if i != loc:
                    temp = f - abs(locations[loc] - locations[i])
                    if temp >= 0:
                        res = (res + foo(i, temp)) % MOD
            return res % MOD

        return foo(start, fuel)
