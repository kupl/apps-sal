class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.memo={}
        self.mod=10**9 + 7
        
        ret=self.dp(locations,start,finish,fuel)
        return ret%self.mod
    
    def dp(self,locations,start,finish,fuel):
        if (start,fuel) in self.memo:
            return self.memo[(start,fuel)]
        if fuel<0:
            return 0
        ans=0
        
        if start==finish:
                ans+=1
        for i,sf in enumerate(locations):
            if i==start:
                continue
            ans+=(self.dp(locations,i,finish,fuel-abs(locations[i]-locations[start])))%self.mod
        self.memo[(start,fuel)]=ans
        return ans
                
        
        
        
        
        
        

