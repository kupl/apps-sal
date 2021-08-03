class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i = 0
        j = 0
        count = 0
        while i < len(grid):
            while j < len(grid[i]):
                print(grid[i][j])
                if grid[i][j] < 0:
                    count += 1
                j += 1

            i += 1
            j = 0
        return count
