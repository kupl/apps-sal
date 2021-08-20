class Solution:

    def getsum(self, prefix, i, j):
        if i < 0 or j < 0:
            return 0
        else:
            return prefix[min(len(prefix), i)][min(len(prefix[0]), j)]

    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = []
        res = 0
        for i in range(m):
            dp.append([0] * n)
        for i in range(m):
            if matrix[i][0] == 1:
                dp[i][0] = 1
                res = res + 1
        for j in range(1, n):
            if matrix[0][j] == 1:
                dp[0][j] = 1
                res = res + 1
        print(res)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] > 0:
                    dp[i][j] = min(min(dp[i - 1][j - 1], dp[i - 1][j]), dp[i][j - 1]) + 1
                    res = res + dp[i][j]
        print(dp)
        return res
