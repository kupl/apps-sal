class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m = len(arr)
        n = len(arr[0])
        dp = [[float('inf') for j in range(n)] for i in range(m)]
        for j in range(n):
            dp[0][j] = arr[0][j]

        for i in range(1, m):
            min_idx = sec_min_idx = None
            for j in range(n):
                if min_idx is None or dp[i - 1][j] < dp[i - 1][min_idx]:
                    sec_min_idx = min_idx
                    min_idx = j
                elif sec_min_idx is None or dp[i - 1][j] < dp[i - 1][sec_min_idx]:
                    sec_min_idx = j

            for j in range(n):
                if j == min_idx:
                    dp[i][j] = dp[i - 1][sec_min_idx] + arr[i][j]
                else:
                    dp[i][j] = dp[i - 1][min_idx] + arr[i][j]

        return min(dp[m - 1])
