class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        import copy
        if not matrix: return 0
        
        dp = copy.deepcopy(matrix)
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        
        total = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                total += dp[i][j]
                    
        return total
