class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xTicks = set()
        yTicks = set()
        for x1, y1, x2, y2 in rectangles:
            xTicks.add(x1)
            xTicks.add(x2)
            yTicks.add(y1)
            yTicks.add(y2)
        xTicksList = sorted(list(xTicks))
        yTicksList = sorted(list(yTicks))

        xTicksDict = {xLable: xi for xi, xLable in enumerate(xTicksList)}
        yTicksDict = {yLable: yi for yi, yLable in enumerate(yTicksList)}

        iMax = len(xTicksList)
        jMax = len(yTicksList)

        grid = [[0 for j in range(jMax)] for i in range(iMax)]
        ans = 0

        for x1, y1, x2, y2 in rectangles:
            for i in range(xTicksDict[x1], xTicksDict[x2]):
                xSide = xTicksList[i + 1] - xTicksList[i]
                for j in range(yTicksDict[y1], yTicksDict[y2]):
                    if grid[i][j] == 0:
                        ans += xSide * (yTicksList[j + 1] - yTicksList[j])
                        grid[i][j] = 1
        # print(grid)
        return ans % (10**9 + 7)
