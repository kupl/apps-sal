import sys


class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def isValid(start, grid):
            valid = []
            (r, c) = start
            (up, right, left, down) = (True, True, True, True)
            if r == 0:
                up = False
            if r == len(grid) - 1:
                down = False
            if c == 0:
                left = False
            if c == len(grid[0]) - 1:
                right = False
            if down and grid[r + 1][c] != 0:
                valid.append((r + 1, c))
            if up and grid[r - 1][c] != 0:
                valid.append((r - 1, c))
            if right and grid[r][c + 1] != 0:
                valid.append((r, c + 1))
            if left and grid[r][c - 1] != 0:
                valid.append((r, c - 1))
            return valid

        def findMaxPath(maxV, path, start, grid):
            validList = isValid(start, grid)
            if not validList:
                if sum(path) > maxV:
                    maxV = sum(path)
            for (r, c) in validList:
                valI = grid[r][c]
                grid[r][c] = 0
                path.append(valI)
                maxV = findMaxPath(maxV, path, (r, c), grid)
                path.pop()
                grid[r][c] = valI
            return maxV
        maxV = -sys.maxsize - 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    val = grid[r][c]
                    grid[r][c] = 0
                    maxV = findMaxPath(maxV, [val], (r, c), grid)
                    grid[r][c] = val
        return maxV
