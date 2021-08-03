class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[0 for i in range(len(arr))]for j in range(len(arr))]
        for i in range(len(arr)):
            dp[0][i] = arr[0][i]
        for i in range(1, len(arr)):
            for j in range(len(arr)):
                m = 9999999
                for k in range(len(arr)):
                    if k != j:
                        m = min(m, dp[i - 1][k])
                dp[i][j] = arr[i][j] + m
        m = 99999999

        for i in range(len(arr)):
            m = min(m, dp[len(arr) - 1][i])
        return m
