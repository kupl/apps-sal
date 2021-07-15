class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Time O(N^2) Space O(N^2)              
        if not grid or len(grid)==0: return 0
        nrows= len(grid)
        ncols= len(grid[0])
        islandid= 2
        maxsize= 0
        idsize= dict()
        
        def getIslandSize(grid, r, c, islandid):
            if not (0<=r<nrows and 0<=c<ncols) or grid[r][c]!=1:
                return 0
            grid[r][c]= islandid
            left= getIslandSize(grid, r, c-1, islandid)
            right= getIslandSize(grid, r, c+1, islandid)
            up = getIslandSize(grid, r-1, c, islandid)
            down= getIslandSize(grid, r+1, c, islandid)
            
            return left+right+up+down+1
        
        # DFS to assign unique islandid to all existing islands
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c]==1:
                    size= getIslandSize(grid, r, c, islandid)
                    maxsize= max(maxsize, size)
                    idsize[islandid]= size
                    islandid+=1
        
        
        # BFS to find if any 0 can be changed to 1 and find maxsize
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c]==0:
                    islands= set()
                    for direction in [[1,0], [0,1], [-1,0], [0,-1]]:
                        newr= r+direction[0]
                        newc= c+direction[1]
                        if 0<=newr<nrows and 0<=newc<ncols and grid[newr][newc]!=0:
                            islands.add(grid[newr][newc])
                    sum=1 # converted 0 to 1
                    for id in islands:
                        sum+=idsize[id]
                    maxsize= max(maxsize, sum)
                    
        return maxsize
                    
#   Only 2 steps:

# Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map.
# Loop every cell == 0, check its connected islands and calculate total islands area.


                
        
    

