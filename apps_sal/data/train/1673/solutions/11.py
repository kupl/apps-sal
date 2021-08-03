class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        # [[1,2,3],
        #  [4,5,6],
        #  [7,8,9]]

        # do a dp where dp(i,j) returns the minimum path starting from (i,j)

        if not arr:
            return 0

        m = len(arr)
        n = len(arr[0])
        INF = float('inf')
        dp = [[INF] * n for _ in range(m)]

        dp[-1] = arr[-1]

        for i in range(m - 2, -1, -1):
            for j in range(n):
                dp[i][j] = min(dp[i + 1][:j] + dp[i + 1][j + 1:]) + arr[i][j]
        print(dp)
        return min(dp[0])
