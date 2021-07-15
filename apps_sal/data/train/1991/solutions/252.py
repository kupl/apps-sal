class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # Trivial DP?
        MOD = 10 ** 9 + 7
        
        n = len(locations)
        
        from functools import lru_cache
        
        @lru_cache(None)
        def ways(index, remFuel):
            #print(\"  \" * indent, index, remFuel)
            if index == finish:
                ans = 1
                possible = True
            else:
                ans = 0
                possible = False
            
            for i in range(n):
                if i == index: continue
                dist = abs(locations[i] - locations[index])
                if dist <= remFuel:
                    possible = True
                    w = ways(i, remFuel - dist)
                    ans = (ans + w) % MOD
                    
            if possible:
                #print(\"  \" * indent, \"answer:\", ans)
                return ans
            
            #print(\"  \" * indent, \"rip\")
            return 0
        
        return ways(start, fuel) % MOD
