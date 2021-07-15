class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = []
        count = 0
        for i in range(len(matrix)):
            inner = []
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    inner.append(0)
                else:
                    if i == 0 or j == 0:
                        inner.append(1)
                        count += 1
                    else:
                        c = 1 + min(dp[i-1][j], min(inner[j-1], dp[i-1][j-1]))
                        inner.append(c)
                        count += c
            dp.append(inner)
        return count
