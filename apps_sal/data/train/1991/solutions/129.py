class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        
        memo={}
        def dfs(x,left_fuel):
            if (x,left_fuel) in memo:
                return memo[(x,left_fuel)]
            s=0
            if x==finish:
                s+=1
            for i in range(len(locations)):
                if x==i:
                    continue
                needed=abs(locations[x]-locations[i])
                #print(needed,left_over)
                if left_fuel>=needed:
                    s+=dfs(i,left_fuel-needed)
                
            
            memo[(x,left_fuel)]=s
            return s
            
        return dfs(start,fuel)%((10**9)+7)
