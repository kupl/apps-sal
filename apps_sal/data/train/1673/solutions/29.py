class Solution:

    def minFallingPathSum(self, A):
        (m, n) = (len(A), len(A[0]))
        dp = A[0].copy()
        for x in range(1, m):
            tmp = [0] * n
            for y in range(n):
                tmp[y] = min((dp[py] for py in range(n) if y != py)) + A[x][y]
            (dp, tmp) = (tmp, dp)
        return min(dp)
