class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ret = 0
        empty = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx = i
                    sy = j
                if grid[i][j] >= 0:
                    empty += 1

        def backtrack(grid, x, y, num_left):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] < 0:
                return
            if grid[x][y] == 2 and num_left == 0:
                self.ret += 1
                return
            neighs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dx, dy in neighs:
                orig_value = grid[x][y]
                grid[x][y] = -1
                backtrack(grid, x + dx, y + dy, num_left - 1)
                grid[x][y] = orig_value

        backtrack(grid, sx, sy, empty - 1)
        return self.ret
