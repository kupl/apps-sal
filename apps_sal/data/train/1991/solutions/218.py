class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
                
        cache = {}
        
        def process(start, fuel):
            if not (start, fuel) in cache:
                ans = 0
                if fuel == 0:
                    ans = 1 if start == finish else 0
                else:
                    if start == finish:
                        ans += 1                  
                    for i in range(n):
                        if i != start and abs(locations[i]-locations[start]) <= fuel:
                            ans += process(i, fuel-abs(locations[i]-locations[start]))
                cache[(start, fuel)] = ans % (10 ** 9 + 7)
            return cache[(start, fuel)]
        
        return process(start, fuel)

