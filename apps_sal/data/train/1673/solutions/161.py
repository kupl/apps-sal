class Solution(object):
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)

        dp = [[0 for i in range(N)] for j in range(N)]

        for j in range(N):
            dp[-1][j] = A[-1][j]

        for i in range(N - 2, -1, -1):
            for j in range(N):
                if j == 0:
                    dp[i][j] = A[i][j] + min(dp[i + 1][1:])
                elif j == N - 1:
                    dp[i][j] = A[i][j] + min(dp[i + 1][:-1])
                else:
                    dp[i][j] = A[i][j] + min(dp[i + 1][:j] + dp[i + 1][j + 1:])

        print(dp)
        return min(dp[0])
