class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        grid = {}
        for x, y in points:
            grid[x] = grid.get(x, []) + [y]
        
        for row in grid.values():
            row.sort()
            
        globalMin = float(\"inf\")
        for row1 in grid:
            for row2 in grid:
                if row1 == row2:
                    continue
                i = j = 0
                preIdx = -1
                while i < len(grid[row1]) and j < len(grid[row2]):
                    if grid[row1][i] < grid[row2][j]:
                        i += 1
                    elif grid[row1][i] > grid[row2][j]:
                        j += 1
                    else:
                        if preIdx != -1:
                            globalMin = min(globalMin, abs(row2 - row1)*(grid[row1][i] - preIdx))
                        preIdx = grid[row1][i]
                        i += 1
                        j += 1
                        
        if globalMin == float(\"inf\"):
            return 0
        return globalMin
