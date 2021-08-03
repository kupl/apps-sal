class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        entries = []
        res = 0
        for r, row in enumerate(grid):
            for c, item in enumerate(row):
                if item == 0: continue
                if c == 0: res = 1
                else:
                    grid[r][c] += grid[r][c-1]
                    entries.append((r, c))
        rows = len(grid)
        for r, c in entries:
            for length in range(grid[r][c], 0, -1):
                if r + length - 1 >= rows\\
                    or grid[r+length-1][c] < length\\
                    or c - length + 1 < 0\\
                    or any(grid[i][c] < 1 or grid[i][c-length+1] < 1\\
                        for i in range(r + 1, r + length - 1)): continue
                res = max(res, length * length)
                break
        return res
