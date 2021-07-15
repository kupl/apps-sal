class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        cache = {}
        
        def dfs(start, fuel):
            # Number of routes from start to finish using less or equal than fuel
            if (start, fuel) not in cache:
                res = 0
                for c in range(len(locations)):
                    if c == start: 
                        continue
                    dist = abs(locations[start] - locations[c])
                    if c == finish and dist <= fuel:
                        res += 1    
                    if dist <= fuel:
                        res += dfs(c, fuel - dist)
                cache[(start, fuel)] = res % (10**9+7)
            
            return cache[(start, fuel)]
        
        return dfs(start, fuel) + int(start == finish)
