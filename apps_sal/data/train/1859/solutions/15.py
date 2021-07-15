class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        result = 0
        
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + matrix[i][j]
        
        for i in range(m):
            for j in range(n):
                for l in range(1,min(m-i,n-j)+1):
                    expected_sum = l**2
                    x,y = i+l, j+l
                    range_sum = dp[x][y] - dp[x][j] - dp[i][y] + dp[i][j]
                    # print(i,j,l,x,y)
                    # print(expected_sum, range_sum)
                    if expected_sum != range_sum:
                        break
                    result += 1
                        
        return result
