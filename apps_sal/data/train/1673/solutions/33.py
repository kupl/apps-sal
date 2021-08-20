class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        cumSum = [[0 for j in range(len(arr[0]) + 1)] for i in range(len(arr) + 1)]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                cumSum[i + 1][j + 1] = arr[i][j] + cumSum[i + 1][j] + cumSum[i][j + 1] - cumSum[i][j]
        dp = [arr[i] for i in range(len(arr))]
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                (i1, j1) = (i + 1, j + 1)
                aboveDP = min([x for (c, x) in enumerate(dp[i - 1]) if c != j])
                dp[i][j] = cumSum[i1][j1] - cumSum[i][j1] - cumSum[i1][j] + cumSum[i][j] + aboveDP
        return min(dp[-1])
