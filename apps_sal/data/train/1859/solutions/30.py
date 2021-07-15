class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        
        dp = [matrix[0][j] for j in range(m)]
        count = sum(dp)
        
        for i in range(1, n):
            new_dp = [matrix[i][j] for j in range(m)]
            
            for j in range(1, m):
                if matrix[i][j] == 1:
                    new_dp[j] = min(dp[j], new_dp[j-1], dp[j-1]) + 1
            
            dp = new_dp
            count += sum(dp)
        
        return count
