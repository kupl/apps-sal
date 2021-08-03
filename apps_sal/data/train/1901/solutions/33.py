from typing import List
import math


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if grid == None or len(grid) == 0 or grid[0] == None or len(grid[0]) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        compSize = [0] * (n * m + 2)

        def dfs(x, y, c):
            nonlocal compSize
            nonlocal grid
            compSize[c] += 1
            grid[y][x] = c
            nextPoints = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
            for point in nextPoints:
                nextX = point[0]
                nextY = point[1]
                if nextX < 0 or nextX == m or nextY < 0 or nextY == n:
                    continue
                if grid[nextY][nextX] == 1:
                    dfs(nextX, nextY, c)
            return

        def calMaxLinkSize(x, y) -> int:
            nonlocal compSize
            nonlocal grid
            uniqueCompNums = []
            nextPoints = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
            for point in nextPoints:
                nextX = point[0]
                nextY = point[1]
                if nextX < 0 or nextX == m or nextY < 0 or nextY == n:
                    continue
                compNum = grid[nextY][nextX]
                if compNum >= 2 and compNum not in uniqueCompNums:
                    uniqueCompNums.append(compNum)
            return sum([compSize[c] for c in uniqueCompNums]) + 1
        compNum = 2
        maxCompSize = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == 1:
                    dfs(x, y, compNum)
                    maxCompSize = max(maxCompSize, compSize[compNum])
                    compNum += 1
        for y in range(n):
            for x in range(m):
                if grid[y][x] == 0:
                    maxCompSize = max(maxCompSize, calMaxLinkSize(x, y))
        return maxCompSize


def __starting_point():
    pass


__starting_point()
