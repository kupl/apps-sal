class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rrange = range(len(grid))
        crange = range(len(grid[0]))
        max_sum = 0

        def helper(row, col, running_sum=0):
            nonlocal max_sum
            if not (row in rrange and col in crange and (grid[row][col] > 0)):
                max_sum = max(max_sum, running_sum)
                return
            running_sum += grid[row][col]
            grid[row][col] *= -1
            helper(row + 1, col, running_sum)
            helper(row, col + 1, running_sum)
            helper(row - 1, col, running_sum)
            helper(row, col - 1, running_sum)
            grid[row][col] *= -1
        for row in rrange:
            for col in crange:
                if grid[row][col] > 0:
                    helper(row, col)
        return max_sum
