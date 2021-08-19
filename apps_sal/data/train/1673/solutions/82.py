class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        dp = [[None for i in range(n)] for i in range(n)]
        for i in range(0, n):
            dp[0][i] = arr[0][i]
        for i in range(1, n):
            for j in range(0, n):
                minList = []
                for k in range(0, n):
                    if k == j:
                        continue
                    minList.append(dp[i - 1][k])
                dp[i][j] = min(minList) + arr[i][j]
        return min(dp[n - 1])
