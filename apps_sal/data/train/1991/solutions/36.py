class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        L = len(locations)
        
        @lru_cache(None)
        def move(loc, remaining):
            #if remaining == 0:
             #   return 0
            
            ans = 0
            if loc == finish:
                ans += 1
            
            for i in range(L):
                f = remaining
                if i == loc:
                    continue
                    
                cost = locations[i] - locations[loc]
                if cost < 0:
                    cost = -cost
                f -= cost
               
                if f < 0:
                    continue
               
                ans += move(i, f)
            
            return ans
        
        return move(start, fuel) % 1000000007
    
    def countRoutes2(self, l: List[int], start: int, fin: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(i: int, f: int) -> int:
            if f < 0:
                return 0
            
            ans = 0
            if i == fin:
                ans = 1
                
            ans += sum(0 if i == j else dfs(j, f - abs(l[j] - l[i])) for j in range(len(l)))
        
        return dfs(start, fuel) % 1000000007
