class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m, n = len(arr), len(arr[0])
        dp = [[float(\"inf\") for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = arr[0][j]
        for i in range(1, m):
            first_min, second_min = float(\"inf\"), dp[i-1][0]
            first_idx, second_idx = 0, 0
            for j in range(n):
                if dp[i-1][j] < first_min:
                    first_min, second_min = dp[i-1][j], first_min
                    first_idx, second_idx = j, first_idx
                elif dp[i-1][j] < second_min:
                    second_min = dp[i-1][j]
                    second_idx = j
            for j in range(n):
                if j == first_idx:
                    dp[i][j] = second_min + arr[i][j]
                else:
                    dp[i][j] = first_min + arr[i][j]
        return min(dp[-1])
