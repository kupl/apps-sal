class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp={}
        def dfs(s,f,fuel):
            if fuel<0:
                return 0
            # print(s,f,fuel)
            ans=0
            if((s,f,fuel) in dp):
                return dp[(s,f,fuel)]
            if s==finish:
                ans+=1
            for i in range(len(locations)):
                if i!=s:
                    ans+=dfs(i,f,fuel-abs(locations[i]-locations[s]))
            ans=ans%(10**9+7)
            dp[(s,f,fuel)]=ans
            return ans
        return dfs(start,finish,fuel)
            

