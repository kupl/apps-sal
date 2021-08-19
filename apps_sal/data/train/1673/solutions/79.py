class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[0] * len(arr[0]) for _ in arr]
        for i in range(len(arr)):
            if i == 0:
                dp[i] = arr[i]
            else:
                for j in range(len(arr[0])):
                    dp[i][j] = self.min_exclude(dp[i - 1], j) + arr[i][j]
        return min(dp[-1])

    def min_exclude(self, array, exclude):
        if len(array) == 0:
            return None
        out = float('inf')
        for i in range(len(array)):
            if i != exclude:
                out = min(out, array[i])
        return out
