class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod=10**9+7
        
        @lru_cache(None)
        def func(a,fuel):
            t=0
            if fuel<0:
                return 0
            if a==finish:
                t+=1
            curr = locations[a]
            for i,item in enumerate(locations):
                if i!=a:
                    t += func(i,max(-1,fuel-abs(curr-item)))
                    t %= mod
            return t % mod
        
        c=func(start,fuel)
        return c % mod

