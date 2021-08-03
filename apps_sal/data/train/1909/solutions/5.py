class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dpdown = [[0] * n for i in range(m)]
        dpright = [[0] * n for i in range(m)]
        for i in range(m):
            cur = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    cur += 1
                    dpright[i][j] = cur
                else:
                    cur = 0
        for j in range(n):
            cur = 0
            for i in range(m - 1, -1, -1):
                if grid[i][j] == 1:
                    cur += 1
                    dpdown[i][j] = cur
                else:
                    cur = 0
        res = 0
        for i in range(m):
            for j in range(n):
                for k in range(min(dpright[i][j], dpdown[i][j])):
                    if dpright[i + k][j] > k and dpdown[i][j + k] > k:
                        res = max(k + 1, res)
        return res**2
