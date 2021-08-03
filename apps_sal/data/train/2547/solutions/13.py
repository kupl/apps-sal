class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid), 0, -1):
            for j in range(len(grid[i - 1]), 0, -1):
                if grid[i - 1][j - 1] < 0:
                    count += 1
                else:
                    break
        return count
