class Solution:
    allGod = -1

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def helper(maxgold, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] > 0:
                temp = grid[i][j]
                self.allGod = max(self.allGod, maxgold + temp)

                grid[i][j] = 0
                helper(maxgold + temp, i - 1, j)
                helper(maxgold + temp, i + 1, j)
                helper(maxgold + temp, i, j - 1)
                helper(maxgold + temp, i, j + 1)
                grid[i][j] = temp

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    helper(0, i, j)
        return self.allGod
