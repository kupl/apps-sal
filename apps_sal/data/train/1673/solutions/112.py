class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m, n = len(arr), len(arr[0])
        dp = arr
        for i in range(1, m):
            for j in range(n):
                acc = float('inf')
                for k in range(n):
                    if k == j:
                        continue
                    acc = min(acc, arr[i - 1][k])
                dp[i][j] = arr[i][j] + acc
        return min(dp[-1])
