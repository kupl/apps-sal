class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        dp = arr[0][:]
        for i in range(1, n):
            right_min = [math.inf] * (n - 1) + [dp[n - 1]]
            for j in range(n - 2, -1, -1):
                right_min[j] = min(right_min[j + 1], dp[j])
            left_min = math.inf
            for j in range(n):
                prev = left_min
                if j < n - 1:
                    prev = min(prev, right_min[j + 1])
                left_min = min(left_min, dp[j])
                dp[j] = prev + arr[i][j]
        return min(dp)
