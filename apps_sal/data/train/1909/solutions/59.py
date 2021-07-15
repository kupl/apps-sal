class Solution:
    def getLeftandTopOnes(self, grid: List[List[int]]):
        leftGrid = [[0] * (len(grid[0])+1) for i in range(len(grid)+1)]
        topGrid = [[0] * (len(grid[0])+1) for i in range(len(grid)+1)]
            
        for row in range(1, len(grid)+1):
            for col in range(1, len(grid[0])+1):
                if (grid[row-1][col-1] == 0):
                    continue
                leftGrid[row][col] = leftGrid[row][col-1] + 1
                topGrid[row][col] = topGrid[row-1][col] + 1
        return (leftGrid, topGrid)          
           
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        leftOnes, topOnes = self.getLeftandTopOnes(grid)        
        
        print(leftOnes)
        print(topOnes)
        
        maxBorder = 0
        for row in range(1, len(grid)+1):
            for col in range(1, len(grid[0])+1):
                dist = min(topOnes[row][col], leftOnes[row][col])
                while (dist > 0):
                    if (topOnes[row][col-dist+1] >= dist and leftOnes[row-dist+1][col] >= dist):
                        maxBorder = max(maxBorder, dist*dist)
                        break
                    dist -= 1
        return maxBorder

