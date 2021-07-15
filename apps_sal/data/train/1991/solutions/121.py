class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @lru_cache(None)
        def go(i, f):
            if f < 0:
                return 0
            if f == 0:
                if i == finish:
                    return 1
                return 0
            
            count = 0
            if i == finish:
                count += 1
                
            for j in range(len(locations)):
                if i != j:
                    count += go(j, f - abs(locations[i] - locations[j]))
            return count
        
        return go(start, fuel) % (10 ** 9 + 7)

