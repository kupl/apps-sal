class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0

            gold = grid[i][j]
            grid[i][j] = 0  # mark as visited

            total = gold + max(dfs(i - 1, j),
                               dfs(i + 1, j),
                               dfs(i, j - 1),
                               dfs(i, j + 1))
            grid[i][j] = gold
            return total

        dp = dict()
        max_gold = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    gold = dfs(i, j)
                    max_gold = max(gold, max_gold)

        return max_gold
