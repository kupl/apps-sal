class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        sum=0
        for i in range(len(dp[0])):
            dp[0][i]=matrix[0][i]
            sum+=dp[0][i]
        print(sum)
        for j in range(1,len(dp)):
            dp[j][0]=matrix[j][0]
            sum+=dp[j][0]
        print(sum)
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if matrix[i][j]==1:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    sum+=dp[i][j]
        
        return sum
                    
    

