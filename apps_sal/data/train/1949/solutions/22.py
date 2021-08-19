class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dsf(r, c, gold):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (grid[r][c] > 0)):
                return
            gold += grid[r][c]
            self.max_gold = max(self.max_gold, gold)
            grid[r][c] *= -1
            dsf(r + 1, c, gold)
            dsf(r - 1, c, gold)
            dsf(r, c + 1, gold)
            dsf(r, c - 1, gold)
            grid[r][c] *= -1
        self.max_gold = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    dsf(r, c, 0)
        return self.max_gold
