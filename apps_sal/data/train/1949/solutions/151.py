class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
       #Approach: Recursive backtracking
        # Keep track of gold at each element and keep calculating max to get the result
         
        
        r, c = len(grid), len(grid[0])
        self.res = 0
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def recurse(i,j, curr):
            self.res = max(curr, self.res)
            
            if i < r and j < c and i>=0 and j >=0 and grid[i][j] != 0:
                gold = grid[i][j]
                
                for x, y in dirs:
                    grid[i][j] = 0
                    recurse(i+x, j+y, curr+gold)
                    grid[i][j] = gold
            
                    
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    recurse(i,j,0)
        
        return self.res
    

