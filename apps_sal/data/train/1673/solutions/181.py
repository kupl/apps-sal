class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        num_rows = len(arr)
        num_cols = len(arr[0])
        dp = [[float('inf') for _ in range(num_cols)] for _ in range(num_rows + 1)]
        for col in range(num_cols):
            dp[0][col] = 0
        for row in range(num_rows):
            dp_r = row + 1
            for col in range(num_cols):
                dp[dp_r][col] = min(dp[dp_r - 1][:col] + dp[dp_r - 1][col + 1:]) + arr[row][col]
        return min(dp[-1])
