class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        max_len = max(m, n)

        for l in range(max_len, 0, -1):

            for i in range(m - l + 1):
                for j in range(n - l + 1):
                    if self.find_board(i, j, l, grid):
                        return l * l
        return 0

    def find_board(self, i, j, l, grid):
        if l == 1:
            return grid[i][j] == 1
        x1, x2 = i, i + l - 1
        for y in range(j, j + l):
            if grid[x1][y] == 0:
                return False
            if grid[x2][y] == 0:
                return False

        y1, y2 = j, j + l - 1
        for x in range(i + 1, i + l - 1):
            if grid[x][y1] == 0:
                return False
            if grid[x][y2] == 0:
                return False

        return True
