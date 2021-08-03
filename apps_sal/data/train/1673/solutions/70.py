class Solution:
    def minFallingPathSum(self, A):
        m, n = len(A), len(A[0])
        dp = A[0].copy()
        for x in range(1, m):
            tmp = [0] * n
            for y in range(n):
                tmp[y] = min(dp[py] + A[x][y] for py in range(n) if y != py)
            dp, tmp = tmp, dp
        return min(dp)
