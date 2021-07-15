from functools import lru_cache
import bisect
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9+7
        
        start_pos = locations[start]
        finish_pos = locations[finish]
        
        locations.sort()
        i = bisect.bisect_left(locations,start_pos)
        j = bisect.bisect_left(locations,finish_pos)
        n = len(locations)

        @lru_cache(None)
        def ways(i,j,fuel):
            if fuel < abs(locations[i]-locations[j]): return 0
            res = 0
            l = r = 1
            if i == j: res += 1
            while i-l >= 0:
                if fuel - abs(locations[i-l]-locations[j]) < 0: break
                res += ways(i-l,j,fuel-abs(locations[i-l]-locations[i]))
                res %= mod
                l += 1
            while i+r < n:
                if fuel - abs(locations[i+r]-locations[j]) < 0: break
                res += ways(i+r,j,fuel-abs(locations[i+r]-locations[i]))
                res %= mod
                r += 1
            return res%mod
            
        return ways(i,j,fuel)
