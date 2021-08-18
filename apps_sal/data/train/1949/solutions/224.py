class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def helper(r, c, total, visited):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0 or (r, c) in visited:
                return

            total += grid[r][c]
            self.maxGold = max(self.maxGold, total)

            helper(r + 1, c, total, visited + [(r, c)])
            helper(r - 1, c, total, visited + [(r, c)])
            helper(r, c + 1, total, visited + [(r, c)])
            helper(r, c - 1, total, visited + [(r, c)])

        gg = 0
        self.maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    helper(i, j, 0, [])
                    gg = max(gg, self.maxGold)
                    self.maxGold = 0

        return gg
