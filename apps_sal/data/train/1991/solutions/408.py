class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        s = locations[start]
        f = locations[finish]
        locations.sort()
        start = locations.index(s)
        finish = locations.index(f)
        
        ph = []
        @lru_cache(None)
        def f(i, fuel):
            nonlocal ph
            if fuel < 0:
                return 0
            routes = 1 if i == finish else 0
                
            loc = locations[i]
            
            j = i + 1
            while j < len(locations) and abs(locations[j] - loc) <= fuel:
                routes += f(j, fuel - abs(locations[j] - loc))
                j += 1
            
            j = i - 1
            while j >= 0 and abs(locations[j] - loc) <= fuel:
                routes += f(j, fuel - abs(locations[j] - loc))
                j -= 1
                
            return routes % 1000000007
        
        return f(start, fuel)
            

