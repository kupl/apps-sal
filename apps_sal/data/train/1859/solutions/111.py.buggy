class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:        
        M=len(matrix)
        N=len(matrix[0])
        dp=[[0 for _ in range(N)]for _ in range(M)]
        res=0  
        for bottom in range(M):             
            for right in range(N):
                if bottom==0 or right==0:
                    dp[bottom][right]=1 if matrix[bottom][right]==1 else 0
                else:
                    dp[bottom][right]=min(dp[bottom-1][right-1],\\
                                          dp[bottom-1][right],\\
                                          dp[bottom][right-1])+1 \\
                                        if matrix[bottom][right]==1 else 0 
                res+=dp[bottom][right]

 
                
        return res
        
