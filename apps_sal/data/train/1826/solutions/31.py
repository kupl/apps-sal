class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        (m, n) = (len(mat[0]), len(mat))
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = sum((sum(mat[col][max(0, j - K):j + K + 1]) for col in range(max(0, i - K), min(i + K + 1, n))))
        return dp
