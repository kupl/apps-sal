class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        ans = 0

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):

                if grid[i][j] != 0:
                    ans = max(ans, self.findGold(grid, i, j))

        return ans

    def findGold(self, grid, row, col):

        if not(0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] == 0:
            return 0

        ans = 0
        temp = grid[row][col]
        grid[row][col] = 0

        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ans = max(ans, self.findGold(grid, row + i, col + j))

        grid[row][col] = temp
        return ans + temp
