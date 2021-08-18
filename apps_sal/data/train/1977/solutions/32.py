'''
Recursion
https://www.youtube.com/watch?v=MnD8KhBHgRo
'''


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        closedIslands = 0
        R, C = len(grid), len(grid[0])

        for i in range(1, R - 1):
            for j in range(1, C - 1):
                if grid[i][j] == 0:
                    if self.isClosedIslands(grid, i, j, R, C):
                        closedIslands += 1

        return closedIslands

    def isClosedIslands(self, grid, i, j, R, C):
        if grid[i][j] == -1 or grid[i][j] == 1:
            return True

        if self.isOnPerimeter(i, j, R, C):
            return False
        grid[i][j] = -1

        left = self.isClosedIslands(grid, i, j - 1, R, C)
        right = self.isClosedIslands(grid, i, j + 1, R, C)
        up = self.isClosedIslands(grid, i - 1, j, R, C)
        down = self.isClosedIslands(grid, i + 1, j, R, C)

        return left and right and up and down

    def isOnPerimeter(self, i, j, R, C):
        return i == 0 or j == 0 or i == R - 1 or j == C - 1
