class Solution:

    def correct(self, i: int, j: int, n: int, m: int) -> bool:
        return 0 <= i < n and 0 <= j < m

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        lu = [[0] * m for i in range(n)]
        rd = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                k = 0
                while self.correct(i - k, j, n, m) and self.correct(i, j - k, n, m) \\
                      and grid[i - k][j] == 1 and grid[i][j - k] == 1:
                    k += 1
                lu[i][j] = k
        for i in range(n):
            for j in range(m):
                k = 0
                while self.correct(i + k, j, n, m) and self.correct(i, j + k, n, m) \\
                      and grid[i + k][j] == 1 and grid[i][j + k] == 1:
                    k += 1
                rd[i][j] = k
        res = 0
        for i in range(n):
            for j in range(m):
                for k in range(rd[i][j] - 1, -1, -1):
                    if lu[i + k][j + k] > k:
                        res = max(res, (k + 1) ** 2)
        return res
