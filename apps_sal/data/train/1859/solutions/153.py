class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        MAXINT = 1 << 30
        
        most_recent_zero_to_left_or_here = [[None] * n for _ in range(m)]
        most_recent_zero_above_or_here = [[None] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    most_recent_zero_to_left_or_here[i][j] = j
                elif j == 0:
                    most_recent_zero_to_left_or_here[i][j] = -1
                else:
                    most_recent_zero_to_left_or_here[i][j] = most_recent_zero_to_left_or_here[i][j - 1]
                    
        for j in range(n):
            for i in range(m):
                if matrix[i][j] == 0:
                    most_recent_zero_above_or_here[i][j] = i
                elif i == 0:
                    most_recent_zero_above_or_here[i][j] = -1
                else:
                    most_recent_zero_above_or_here[i][j] = most_recent_zero_above_or_here[i - 1][j]
                    
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = matrix[i][0]
            
        for j in range(n):
            dp[0][j] = matrix[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                limit = min(i - most_recent_zero_above_or_here[i][j], j - most_recent_zero_to_left_or_here[i][j])
                old = dp[i - 1][j - 1]
                dp[i][j] = min(1 + old, limit)
                
        return sum(dp[i][j] for i in range(m) for j in range(n))

