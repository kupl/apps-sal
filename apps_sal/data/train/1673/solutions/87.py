class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
        for i in range(len(dp)):
            dp[0][i] = arr[0][i]
        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] = min((arr[i][j] + dp[i - 1][k] for k in range(1, len(dp[i]))))
                elif j == len(dp[i]) - 1:
                    dp[i][j] = min((arr[i][j] + dp[i - 1][k] for k in range(len(dp[i]) - 1)))
                else:
                    left_max = min((arr[i][j] + dp[i - 1][k] for k in range(j)))
                    right_max = min((arr[i][j] + dp[i - 1][k] for k in range(j + 1, len(dp[i]))))
                    dp[i][j] = min(left_max, right_max)
        return min(dp[-1])
