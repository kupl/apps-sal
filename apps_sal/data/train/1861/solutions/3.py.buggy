class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        \"\"\"
        maxRow = {(col pair): largest row index}
        
        for every col pair, if in maxRow, update globalMin, update maxRow
        
        O(m * n^2)
        \"\"\"
        grid = {}       # {row: [cols with 1]}
        for x, y in points:
            grid[x] = grid.get(x, []) + [y]
        for value in grid.values():
            value.sort()
        
        minArea = float(\"inf\")
        maxRow = {}
        for row in sorted(grid.keys()):
            n = len(grid[row])
            for i in range(n):
                for j in range(i + 1, n):
                    pair = (grid[row][i], grid[row][j])
                    if pair in maxRow:
                        rowPre = maxRow[pair]
                        minArea = min(minArea, (row - rowPre) * (pair[1] - pair[0]))
                    maxRow[pair] = row
        return minArea if minArea != float(\"inf\") else 0
