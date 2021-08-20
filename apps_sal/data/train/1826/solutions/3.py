class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        answer = [[0] * n for _ in range(m)]
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = mat[i][j]
                else:
                    dp[i][j] = dp[i][j - 1] + mat[i][j]
        for i in range(m):
            for j in range(n):
                for x in range(i - K, i + K + 1):
                    if x >= 0 and x < m:
                        if j - K <= 0:
                            if j + K >= n:
                                answer[i][j] += dp[x][-1]
                            else:
                                answer[i][j] += dp[x][j + K]
                        elif j - K <= n:
                            if j + K >= n:
                                answer[i][j] += dp[x][-1] - dp[x][j - K - 1]
                            else:
                                answer[i][j] += dp[x][j + K] - dp[x][j - K - 1]
        return answer
