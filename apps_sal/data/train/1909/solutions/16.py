class Solution:

    def getLeftandTopOnes(self, grid: List[List[int]]):
        leftGrid = [[0] * len(grid[0]) for i in range(len(grid))]
        topGrid = [[0] * len(grid[0]) for i in range(len(grid))]
        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                if i > 0:
                    if grid[i - 1][j] == 1:
                        topGrid[i][j] = topGrid[i - 1][j] + 1
                    elif grid[i - 1][j] == 0:
                        topGrid[i][j] = 0
                if j > 0:
                    if grid[i][j - 1] == 1:
                        leftGrid[i][j] = leftGrid[i][j - 1] + 1
                    elif grid[i][j - 1] == 0:
                        leftGrid[i][j] = 0
                j += 1
            i += 1
        return (leftGrid, topGrid)

    def getRightandDownOnes(self, grid: List[List[int]]):
        rightGrid = [[0] * len(grid[0]) for i in range(len(grid))]
        downGrid = [[0] * len(grid[0]) for i in range(len(grid))]
        i = len(grid) - 1
        while i >= 0:
            j = len(grid[0]) - 1
            while j >= 0:
                if i < len(grid) - 1:
                    if grid[i + 1][j] == 1:
                        downGrid[i][j] = downGrid[i + 1][j] + 1
                    elif grid[i + 1][j] == 0:
                        downGrid[i][j] = 0
                if j < len(grid[0]) - 1:
                    if grid[i][j + 1] == 1:
                        rightGrid[i][j] = rightGrid[i][j + 1] + 1
                    elif grid[i][j + 1] == 0:
                        rightGrid[i][j] = 0
                j -= 1
            i -= 1
        return (rightGrid, downGrid)

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        (leftOnes, topOnes) = self.getLeftandTopOnes(grid)
        print(leftOnes)
        print(topOnes)
        (rightOnes, downOnes) = self.getRightandDownOnes(grid)
        print(rightOnes)
        print(downOnes)
        maxBorder = 0
        i = 0
        seenOne = False
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                if grid[i][j] == 1:
                    seenOne = True
                    length = min(topOnes[i][j], leftOnes[i][j])
                    while length >= 0:
                        if i - length < 0 or j - length < 0:
                            length -= 1
                            continue
                        if length == 0:
                            break
                        if topOnes[i][j - length] >= length and leftOnes[i - length][j] >= length:
                            break
                        length -= 1
                    maxBorder = max(maxBorder, length)
                j += 1
            i += 1
        if not seenOne:
            return 0
        else:
            return (maxBorder + 1) ** 2
