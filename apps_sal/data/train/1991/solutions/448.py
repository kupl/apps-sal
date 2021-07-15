class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n=len(locations)
        dp=[[ 0 for i in range(n)] for j in range(fuel+1)]
        dp[fuel][start]=1
        for f in range(fuel,-1,-1):
            for pos in range(n):
                for dest in range(n):
                    travel=abs(locations[pos]-locations[dest])
                    if pos!=dest and f>=travel:
                        dp[f-travel][dest]+=dp[f][pos]
            
            
        ans=0
        for k in range(fuel+1):
            ans=(ans+dp[k][finish])%(10**9+7)
        
        return ans

