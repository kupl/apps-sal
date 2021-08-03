class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * cols
        maxLen = 1 if sum(dp) > 0 else 0
        for i in range(0, rows):
            for j in range(0, cols):
                if matrix[i][j] == '1':
                    if j == 0:
                        dp[j] = int(matrix[i][j])
                    else:
                        k = min(dp[j], dp[j - 1])
                        dp[j] = (k + 1) if matrix[i - k][j - k] == '1' else k
                    maxLen = max(maxLen, dp[j])
                else:
                    dp[j] = 0
        return maxLen * maxLen
