class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        A = arr
        m = len(A)
        n = len(A[0])
        if m == n == 1:
            return A[0][0]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cell = float('inf')
                for k in range(1, n + 1):
                    if j == k:
                        continue
                    cell = min(cell, dp[i - 1][k])
                dp[i][j] = cell + A[i - 1][j - 1]
        return min(dp[-1][1:])
