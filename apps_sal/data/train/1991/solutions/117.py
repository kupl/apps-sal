import functools


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @functools.lru_cache(10**9)
        def findRoutes(start, finish, fuel, n):
            r = 0
            if(fuel < 0):
                return 0
            if(start == finish):
                r += 1
            for i in range(n):
                if(i != start):
                    r += findRoutes(i, finish, fuel - abs(locations[i] - locations[start]), n)
            return r
        return findRoutes(start, finish, fuel, len(locations)) % (10**9 + 7)
