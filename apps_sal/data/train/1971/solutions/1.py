class Solution:

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        (n, m) = (len(matrix), len(matrix[0]))
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
        for j in range(m):
            dp[0][j] = int(matrix[0][j])
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        ans = 0
        for i in range(n):
            ans = max(ans, max(dp[i]))
        return ans ** 2
