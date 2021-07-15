class Solution:
    def countSquares(self, dp):
        if len(dp)==0 or len(dp[0])==0:
            return 0
        for i,row in enumerate(dp):
            for j,val in enumerate(row):
                if val==1:
                    left=dp[i][j-1] if j>0 else 0
                    up=dp[i-1][j] if i>0 else 0
                    diag=dp[i-1][j-1] if i>0 and j>0 else 0
                    dp[i][j]=min((left,up,diag))+1
                else:
                    dp[i][j]=0
        return sum(map(sum,dp))

