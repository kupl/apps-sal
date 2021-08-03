class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        n = min(rows, cols)
        rs = [row[:] for row in grid]
        cs = [row[:] for row in grid]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    if row:
                        cs[row][col] = cs[row - 1][col] + 1
                    if col:
                        rs[row][col] = rs[row][col - 1] + 1
        for size in range(n, 0, -1):
            for row in range(rows - size + 1):
                for col in range(cols - size + 1):
                    if min(cs[row + size - 1][col], cs[row + size - 1][col + size - 1], rs[row][col + size - 1], rs[row + size - 1][col + size - 1]) >= size:
                        return size * size
        return 0
