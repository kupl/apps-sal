\"\"\"
dfs timeO(mn) spaceO(mn)
1. get area of an island (similar to LC200, 695)
2. set visited nodes to 2,3,4, ... for 1st, 2nd,3rd ... islands
3. store the maxArea of islands
4. for each 0, check its 4 neighbors.if a neighbor is not 0, get its area. try to fill this 0 and connect its neighbor islands
\"\"\"

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        self.grid = grid
        mark = 1
        mark2island = {}
        mark2island[0]=0
        maxArea = 0
        
        # get area of each island; mark them as 2,3,... timeO(mn)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 1: # found a new island
                    mark+=1
                    area = self.getArea(i,j,mark)
                    mark2island[mark] = area
                    maxArea = max(maxArea,area)
        
        # check each 0, try connect it to 4 neighbors timeO(mn)
        maxNewIsland = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 0: # found a new 0
                    tempArea = 1 # the grid itself
                    neighborIslands = set() # must use set to avoid duplicates
                    for d in ([0,1],[0,-1],[1,0],[-1,0]):
                        neighborIslands.add(self.getMark(i+d[0], j+d[1]))
                    for m in neighborIslands:
                        tempArea+=mark2island[m]
                    # print(i,j,tempArea)
                    maxNewIsland = max(maxNewIsland,tempArea)
        # print(self.grid)
        return max(maxNewIsland,maxArea) # the max can be an existing island
        
                    
        
    def getArea(self,i,j,mark):
        if 0<=i<len(self.grid) and 0<=j<len(self.grid[0]) and self.grid[i][j]==1: 
            self.grid[i][j] = mark # set visited node to 'mark' (e.g. 2,3,4)
            return 1+self.getArea(i+1,j,mark)+self.getArea(i-1,j,mark)+self.getArea(i,j+1,mark)+self.getArea(i,j-1,mark)
        return 0
    
    def getMark(self,i,j): # get a grid's mark
        if 0<=i<len(self.grid) and 0<=j<len(self.grid[0]):
            return self.grid[i][j]
        return 0
        
        
