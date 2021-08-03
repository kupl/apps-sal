class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [arr[i] for i in range(len(arr))]

        for i in range(1, len(arr)):
            for j in range(len(arr[0])):
                opts = [(arr[i][j] + x) for c, x in enumerate(arr[i - 1]) if c != j]
                dp[i][j] = min(opts)
        return min(dp[-1])
