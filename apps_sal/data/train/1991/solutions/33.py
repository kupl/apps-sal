import functools
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @lru_cache(maxsize=None)
        def s(city, left):
            if left < 0:
                return 0
            l = locations[city]
            p, q = bisect_left(locations, l - left), bisect_right(locations, l + left)
            return (sum(s(i, left - abs(l - locations[i])) for i in range(p, q) if i != city) + (1 if city == finish else 0)) % MOD
            
        sp, fp = locations[start], locations[finish]
        locations.sort()
        start, finish = bisect_left(locations, sp), bisect_left(locations, fp)
        MOD = 10 ** 9 + 7
        return s(start, fuel)
