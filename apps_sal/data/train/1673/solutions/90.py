class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[0] * len(arr[0]) for _ in range(len(arr))]
        dp[0] = arr[0][:]
        for i in range(1, len(arr)):
            for j in range(len(arr[0])):
                dp[i][j] = min([arr[i][j] + dp[i-1][k] for k in range(len(arr[0])) if k != j])
        return min(dp[-1])
