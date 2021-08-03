class Solution:
    class Graph:
        def __init__(self, g):
            self.r = len(g)
            self.c = len(g[0])
            self.graph = g

        def isSafe(self, r, c, notvisited):
            return r >= 0 and r < self.r and c >= 0, c < self.c and notvisited[r][c] and self.graph[r][c] == 1

    def countSquares(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        cnt = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j], dp[i][j + 1]) + 1
                    cnt += dp[i + 1][j + 1]
        return cnt
