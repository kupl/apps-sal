class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0] = list(map(lambda x: int(x), matrix[0]))
        maxLength = 1 if 1 in dp[0] else 0
        for i in range(1, m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                maxLength = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                    maxLength = max(maxLength, dp[i][j])
        return maxLength ** 2
