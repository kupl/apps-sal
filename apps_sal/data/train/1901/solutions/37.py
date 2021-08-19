
class Solution:

    def largestIsland(self, grid):
        m, n, largest, areaMap = len(grid), len(grid[0]), 0, {}
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def getIsland(cords, cord):
            if cord[0] < 0 or cord[0] >= m or cord[1] < 0 or cord[1] >= n or not grid[cord[0]][cord[1]]:
                return
            if (cord[0], cord[1]) not in cords:
                cords.add(cord)
                for dir in dirs:
                    getIsland(cords, (cord[0] + dir[0], cord[1] + dir[1]))
        # get {(i, j), set()} kind of map for each (i, j) where set includes all (i, j)s in the connected area
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in areaMap:
                    cubes = set()
                    getIsland(cubes, (i, j))
                    largest = max(largest, len(cubes))
                    for c in cubes:
                        areaMap[c] = cubes
        # traverse again to find any possible gap and walk thru the surrounding areas to find the largest
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    area, areaSet = 0, set()
                    for dir in dirs:
                        if (i + dir[0], j + dir[1]) in areaMap and (i + dir[0], j + dir[1]) not in areaSet:
                            area += len(areaMap[(i + dir[0], j + dir[1])])
                            areaSet |= areaMap[(i + dir[0], j + dir[1])]
                    largest = max(largest, area + 1)

        return largest
