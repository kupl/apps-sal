class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res=0
        dp=matrix
        r=len(dp)
        c=len(dp[0])
                  
        for i in range(1,r):
            for j in range(1,c):
                if dp[i][j]==0:
                    continue
                if dp[i-1][j]!=0 and dp[i-1][j-1]!=0 and dp[i][j-1]!=0:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
        for i in dp:
            res+=sum(i)
        return res
