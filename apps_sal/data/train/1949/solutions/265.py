class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # DFS
        
        self.res = 0
        rows = len(grid)
        cols = len(grid[0])
        
        
        def backtrace(i,j,tot):
            self.res = max(self.res,tot+grid[i][j]) # 更新最大值
            gridVal = grid[i][j]
            grid[i][j] = 0 # 以防回退
            
            for (a,b) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if a >=0 and b >=0 and a < rows and b < cols and grid[a][b]!=0:
                    backtrace(a,b,tot+gridVal)
            # DFS需要reset
            grid[i][j] = gridVal
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=0:
                    backtrace(i,j,0)
        return self.res
