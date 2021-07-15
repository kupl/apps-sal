class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10**9 + 7
        @lru_cache(None)
        def go(x, remain):
            #print(x, remain)
                
            if remain < 0:
                return 0
            
            ret = 0
            if x == finish:
                ret = 1
                    
            for i in range(0, n):
                if i == x:
                    continue
                ret += go(i,remain - abs(locations[x] - locations[i]))
                ret %= mod
                
            return ret % mod
        
        ans = go(start, fuel) % mod
        
        return ans
                
        
        

