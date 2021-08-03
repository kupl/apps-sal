class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # dp[i] n routes if last visited city is  
        
        # dp[l,f] : ways from l to end with fuel f
        n = len(locations)
        dp = [[0]*(fuel+1) for _ in range(n)]
            
        dp[finish][0] = 1
        for f in range(1,fuel+1):
            for i,loc in enumerate(locations):
                dp[i][f] = sum(dp[j][f-abs(l-loc)] for j,l in enumerate(locations) if f>=abs(l-loc) and l!=loc)
                
        dq = [0]*n
        for i in range(n):
            dq[i] = sum(dp[i])
                
        #print(dq,sep='\
')
                
        return dq[start] % (10**9+7)
