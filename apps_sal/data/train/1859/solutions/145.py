class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = copy.deepcopy(matrix)
        counter = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0 or dp[i][j] == 0:
                    counter += dp[i][j]
                    continue
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    counter += dp[i][j]
        
        return counter
