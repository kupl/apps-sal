class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])
        self.res = 0

        def backtrack(i, j, cur_gold):
            self.res = max(self.res, cur_gold)

            if 0 <= i < R and 0 <= j < C and grid[i][j] != 0:
                gold = grid[i][j]
                grid[i][j] = 0
                backtrack(i + 1, j, cur_gold + gold)
                backtrack(i - 1, j, cur_gold + gold)
                backtrack(i, j + 1, cur_gold + gold)
                backtrack(i, j - 1, cur_gold + gold)
                grid[i][j] = gold

        for i in range(R):
            for j in range(C):
                if grid[i][j] != 0:
                    backtrack(i, j, 0)
        return self.res
