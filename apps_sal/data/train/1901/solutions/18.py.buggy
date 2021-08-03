class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        \"\"\"
        Best explanation: https://www.youtube.com/watch?v=_426VVOB8Vo
        \"\"\"
        
        if not grid:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        
        
        def dfsIslandSize(r, c, islandID, size):
            if r < 0 or r > rows - 1 or c < 0 or c > columns - 1 or grid[r][c] != 1:
                return size
            
            grid[r][c] = islandID
            size += 1
            
            size = dfsIslandSize(r-1, c, islandID, size)
            size = dfsIslandSize(r+1, c, islandID, size)
            size = dfsIslandSize(r, c-1, islandID, size)
            size = dfsIslandSize(r, c+1, islandID, size)
            
            return size
            
        
        def calculateJoinedIslandsSize(r, c):
            neighbors = set()
            
            if r - 1 >= 0 and grid[r-1][c] > 1:
                neighbors.add(grid[r-1][c])
                
            if c - 1 >= 0 and grid[r][c-1] > 1:
                neighbors.add(grid[r][c-1])
                
            if r + 1 <= rows - 1 and grid[r+1][c] > 1:
                neighbors.add(grid[r+1][c])
                
            if c + 1 <= columns - 1 and grid[r][c+1]:
                neighbors.add(grid[r][c+1])
                
            
            size = 1 # becouse we converted the current 0 to a 1
            for neighbor in list(neighbors):
                size += d[neighbor]
                
            return size                    
        

        
        islandID = 2
        d = {}
        maxSize = 0
        
        # Iterate first to mark grid with islandID and calculate island sizes
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    size = dfsIslandSize(r, c, islandID, 0)
                    d[islandID] = size
                    islandID += 1
                    maxSize = max(maxSize, size)
        
        # Iterate over grid. Convert 0 to 1 and calculate joined islands size
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    size = calculateJoinedIslandsSize(r, c)
                    maxSize = max(maxSize, size)
                    
        return maxSize
            
            
        
