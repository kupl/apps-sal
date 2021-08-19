class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m = len(arr)
        dp = [[0 for x in range(m)] for x in range(m)]
        for i in range(m):
            for j in range(m):
                if i == 0:
                    dp[i][j] = arr[i][j]
                else:
                    temp = dp[i - 1].copy()
                    temp.pop(j)
                    dp[i][j] = arr[i][j] + min(temp)
        return min(dp[m - 1])
