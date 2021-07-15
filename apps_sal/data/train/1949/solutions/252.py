class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        rows = len(grid)
        cols = len(grid[0])
        
        self.ans = 0
        
        def dfs(grid, row, col, currg):
            
            self.ans = max(self.ans, currg)
            
            if row >=0 and row<rows and col>=0 and col<cols and grid[row][col] != 0:
                ga = grid[row][col]
                
                grid[row][col] = 0
                # neighbors = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]
                # for x, y in neighbors:
                #     dfs(grid, x, y, currg+ga)
                
                for p in [(1, 0), (-1, 0), (0,1), (0, -1)]:
                    dfs(grid, row + p[0], col + p[1], currg+ga)
                    
                grid[row][col] = ga
                
                        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] != 0:
                    dfs(grid,x,y,0)
        
        return self.ans
                   
                        
                    
        
        

