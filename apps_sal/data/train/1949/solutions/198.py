class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def neighbor(r, c):
            for dr, dc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= dr < nrow and 0 <= dc < ncol:
                    yield dr, dc

        self.cur_gold = 0
        self.max_gold = 0

        def backtrack(r, c):
            if grid[r][c] == 0:  # no gold, not allowed to process
                return
            gold_cnt = grid[r][c]
            self.cur_gold += gold_cnt

            self.max_gold = max(self.max_gold, self.cur_gold)
            grid[r][c] = 0

            for dr, dc in neighbor(r, c):
                backtrack(dr, dc)

            grid[r][c] = gold_cnt  # backtrack
            self.cur_gold -= gold_cnt

        nrow, ncol = len(grid), len(grid[0])
        for r in range(nrow):
            for c in range(ncol):
                backtrack(r, c)

        return self.max_gold
