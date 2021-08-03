class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [0] * len(arr[0])
        for r, row in enumerate(arr):
            for c in range(len(row)):
                row[c] += min(dp[:c] + dp[c + 1:])
            dp = row[:]
        return min(dp)
