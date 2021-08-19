class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m = len(arr)
        print(m)
        if m == 1:
            return min(arr[0])
        dp = [[0 for x in range(m)] for x in range(m)]
        for i in range(m):
            for j in range(m):
                if i == 0:
                    dp[i][j] = arr[i][j]
                else:
                    minn = 1000
                    for k in range(0, m):
                        if k != j and dp[i - 1][k] < minn:
                            minn = dp[i - 1][k]
                    dp[i][j] = minn + arr[i][j]
        print(dp)
        return min(dp[m - 1])
