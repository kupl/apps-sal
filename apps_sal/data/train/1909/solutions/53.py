class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        max_len = max(m, n)

        row_count = [[grid[i][0]] for i in range(m)]
        for i in range(m):
            for j in range(1, n):
                if grid[i][j]:
                    row_count[i].append(row_count[i][j - 1] + 1)
                else:
                    row_count[i].append(0)

        col_count = [[grid[0][j] for j in range(n)]]
        for i in range(1, m):
            col_count.append([])
            for j in range(n):
                if grid[i][j]:
                    col_count[i].append(col_count[i - 1][j] + 1)
                else:
                    col_count[i].append(0)

        for l in range(max_len, 0, -1):
            for i in range(m - l + 1):
                for j in range(n - l + 1):
                    if self.find_board(i, j, l, row_count, col_count):
                        return l * l
        return 0

    def find_board(self, i, j, l, row_count, col_count):
        if l == 1:
            return row_count[i][j] == 1

        l = l - 1
        x, y = i + l, j + l

        if row_count[i][y] <= l:
            return False

        if row_count[x][y] <= l:
            return False

        if col_count[x][j] <= l:
            return False

        if col_count[x][y] <= l:
            return False

        return True
