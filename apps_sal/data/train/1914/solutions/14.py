class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)//2
        dp=[ [0 for _ in range(n+1)] for _ in range(n+1) ]
        
        for i in range(1,n+1):
            dp[i][0]=dp[i-1][0] +costs[i-1][0]
        
        for j in range(1,n+1):
            dp[0][j] = dp[0][j-1] + costs[j-1][1]
            
        for a in range(1,n+1):
            for b in range(1,n+1):
                dp[a][b]=min(dp[a-1][b]+costs[a+b-1][0],dp[a][b-1]+costs[a+b-1][1])
        #print (dp)
        return dp[n][n]
        

