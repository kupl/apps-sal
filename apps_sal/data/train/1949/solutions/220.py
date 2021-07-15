class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        \"\"\"
        :type grid: List[List[int]]
        :rtype: int
        \"\"\"
        self.grid = grid
        #self.visited = []
        self.total = 0
        
        for i in range(len(grid)):
            for z in range(len(grid[0])):
                self.pathfinder(i, z, 0, [])
                self.visited = []
    
        return self.total
    
    def pathfinder(self, i, z, curVal, visited):
        visited.append((i, z))
        visitedCopy = visited.copy()
        curVal += self.grid[i][z]
        if curVal > self.total:
            self.total = curVal
        if i - 1 >= 0 and self.grid[i-1][z] != 0 and (i-1, z) not in visited:
            self.pathfinder(i-1, z, curVal, visited)
            visited = visitedCopy.copy()
        if i + 1 <= len(self.grid)-1 and self.grid[i+1][z] != 0 and (i+1, z) not in visited:
            self.pathfinder(i+1, z, curVal, visited)
            visited = visitedCopy.copy()
        if z - 1 >= 0 and self.grid[i][z-1] != 0 and (i, z-1) not in visited:
            self.pathfinder(i, z-1, curVal, visited)
            visited = visitedCopy.copy()
        if z + 1 <= len(self.grid[0])-1 and self.grid[i][z+1] != 0 and (i, z+1) not in visited:
            self.pathfinder(i, z+1, curVal, visited)
             
