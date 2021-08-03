class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def fun(g, i0, i1, n1, t1, f2, row, col):
            if n1 == t1:
                if abs(f2[1] - i1) + abs(f2[0] - i0) == 1:
                    self.ans += 1
            else:
                if i1 + 1 != col and g[i0][i1 + 1] == 0:
                    g[i0][i1 + 1] = 1
                    fun(g, i0, i1 + 1, n1 + 1, t1, f2, row, col)
                    g[i0][i1 + 1] = 0
                if i1 != 0 and g[i0][i1 - 1] == 0:
                    g[i0][i1 - 1] = 1
                    fun(g, i0, i1 - 1, n1 + 1, t1, f2, row, col)
                    g[i0][i1 - 1] = 0
                if i0 + 1 != row and g[i0 + 1][i1] == 0:
                    g[i0 + 1][i1] = 1
                    fun(g, i0 + 1, i1, n1 + 1, t1, f2, row, col)
                    g[i0 + 1][i1] = 0
                if i0 != 0 and g[i0 - 1][i1] == 0:
                    g[i0 - 1][i1] = 1
                    fun(g, i0 - 1, i1, n1 + 1, t1, f2, row, col)
                    g[i0 - 1][i1] = 0

        self.ans = 0
        i0, i1, t1 = 0, 0, 0
        f2 = [0, 0]
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    t1 += 1
                elif grid[i][j] == 1:
                    i0, i1 = i, j
                elif grid[i][j] == 2:
                    f2 = [i, j]
        fun(grid, i0, i1, 0, t1, f2, row, col)
        return self.ans
