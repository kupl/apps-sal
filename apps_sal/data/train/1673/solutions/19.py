class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m, n = len(arr), len(arr[0])
        dp = [[0] * n for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(n):
                m0, m1 = heapq.nsmallest(2, dp[i - 1])
                dp[i][j] = arr[i - 1][j] + (m0 if dp[i - 1][j] != m0 else m1)

        return min(dp[-1])
