class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1]*(fuel+1) for i in range(len(locations))]
        def dfs(start,fuel):
            if fuel<0:
                return 0
            if dp[start][fuel]>-1:
                return dp[start][fuel]
            if start==finish:
                res=1
            else:
                res=0
            for i in range(len(locations)):
                if i!=start:
                    res+=dfs(i,fuel-abs(locations[i]-locations[start]))
            dp[start][fuel]=res%(10**9+7)  
            return dp[start][fuel]
             
        return dfs(start,fuel)
    
    

