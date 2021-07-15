class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[]
        for i in range(m):
            temp=[0]*n
            dp.append(temp)
        for j in range(n):
            if(matrix[0][j]==1):
                dp[0][j]=1
        for i in range(1,m,1):
            if(matrix[i][0]==1):
                dp[i][0]=1
        for i in range(1,m,1):
            for j in range(1,n,1):
                if(matrix[i][j]==1):
                    dp[i][j]=min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1])+1
        ans=0
        for k in range(m):
            for l in range(n):
                ans+=dp[k][l]
        return ans
                

