class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        m = len(arr[0])
        dp = [[sys.maxsize] * m for i in range(n)]
        for j in range(m):
            dp[0][j] = arr[0][j]
        for i in range(1, n):
            for j in range(m):
                val = sys.maxsize
                for k in range(m):
                    if k != j:
                        val = min(val, dp[i - 1][k])
                dp[i][j] = val + arr[i][j]
        return min(dp[-1][:])
