class Solution:
    def countSquares(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        m,n = len(M), len(M[0])
        
        rowCounts = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if M[i][j]:
                    rowCounts[i][j] = 1+rowCounts[i][j-1] if j>0 else 1
        
        colCounts = [[0]*n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if M[i][j]:
                    colCounts[i][j]=1+colCounts[i-1][j] if i>0 else 1
               
        dp = [[0]*n for _ in range(m)]
        out=0
        for i in range(m):
            for j in range(n):
                if M[i][j]:
                    if i==0 or j ==0:
                        dp[i][j] = min(rowCounts[i][j],colCounts[i][j])
                    else:
                        dp[i][j] = min(rowCounts[i][j],colCounts[i][j],1+dp[i-1][j-1])
                    out+=dp[i][j]
        return out

