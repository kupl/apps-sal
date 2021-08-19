class Solution:

    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            row = 0
            col = 0
            for j in range(len(grid[i])):
                if grid[i][j]:
                    ans += 1
                row = max(row, grid[i][j])
                col = max(col, grid[j][i])
            ans += row + col
        return ans
