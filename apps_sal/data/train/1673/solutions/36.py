class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        cumSum = [[0 for j in range(len(arr[0]) + 1)] for i in range(len(arr) + 1)]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                cumSum[i + 1][j + 1] = arr[i][j] + cumSum[i + 1][j] + cumSum[i][j + 1] - cumSum[i][j]
        dp = [arr[i] for i in range(len(arr))]
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                (csR, csC) = (i + 1, j + 1)
                (leftR, leftC) = (i, j + 1)
                (topR, topC) = (i + 1, j)
                (addR, addC) = (i, j)
                aboveDP = min([x for (c, x) in enumerate(dp[i - 1]) if c != j])
                dp[i][j] = cumSum[csR][csC] - cumSum[leftR][leftC] - cumSum[topR][topC] + cumSum[addR][addC] + aboveDP
        return min(dp[-1])
