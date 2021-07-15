class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        if not mat or not mat[0]:
            return 0
        
        m = len(mat)
        n = len(mat[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # dp only counts num from looking left
                    dp[i+1][j+1] = dp[i+1][j] + 1
                    res += dp[i+1][j+1]
                    
                    minOnes = dp[i+1][j+1]
                    k = i-1
                    while k >=0 and mat[k][j] == 1:
                        minOnes = min(minOnes, dp[k+1][j+1])
                        res += minOnes
                        k -= 1
                        
                        
        return res

