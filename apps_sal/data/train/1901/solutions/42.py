class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        nrows = len(grid)
        ncols = len(grid[0])
        islandid = 2
        maxsize = 0
        idsize = dict()

        def getIslandSize(grid, r, c, islandid):
            if not (0 <= r < nrows and 0 <= c < ncols) or grid[r][c] != 1:
                return 0
            grid[r][c] = islandid
            left = getIslandSize(grid, r, c - 1, islandid)
            right = getIslandSize(grid, r, c + 1, islandid)
            up = getIslandSize(grid, r - 1, c, islandid)
            down = getIslandSize(grid, r + 1, c, islandid)

            return left + right + up + down + 1

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    size = getIslandSize(grid, r, c, islandid)
                    maxsize = max(maxsize, size)
                    idsize[islandid] = size
                    islandid += 1

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 0:
                    islands = set()
                    for direction in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        newr = r + direction[0]
                        newc = c + direction[1]
                        if 0 <= newr < nrows and 0 <= newc < ncols and grid[newr][newc] != 0:
                            islands.add(grid[newr][newc])
                    sum = 1
                    for id in islands:
                        sum += idsize[id]
                    maxsize = max(maxsize, sum)

        return maxsize
