class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])

        dp = [[0 for _ in range(N)] for _ in range(M)]

        dp = matrix[:][:]

        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 1:
                    dp[i][j] = min([dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]]) + 1

        res = 0

        for i in range(M):
            for j in range(N):
                if dp[i][j] > 0:
                    for size in range(1, dp[i][j] + 1):
                        res += 1

        return res
