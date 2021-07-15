class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0] * n for _ in range(m)]
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + mat[i][j]
        
        for i in range(m):
            for j in range(n):
                r1, c1, r2, c2 = max(0, i-K), max(0, j-K), min(m, i+K+1), min(n, j+K+1)
                res[i][j] = dp[r2][c2] + dp[r1][c1] - dp[r2][c1] - dp[r1][c2]
        return res
