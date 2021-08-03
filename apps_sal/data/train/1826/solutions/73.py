class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat[0]), len(mat)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

        for i in range(n):
            for j in range(m):
                l, r = max(0, i - K), max(0, j - K)
                p, q = min(n, i + K + 1), min(m, j + K + 1)
                mat[i][j] = dp[p][q] - dp[p][r] - dp[l][q] + dp[l][r]
        return mat
