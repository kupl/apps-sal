class Solution:
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        self.res = 0
        for i in range(self.row):
            for j in range(self.col):
                self.dfs(i, j, 0, grid)
        return self.res
    
    def dfs(self, i, j, addition, grid):
        if(i<0 or j<0 or i>=self.row or j>=self.col or grid[i][j] == 0 or grid[i][j] == \"#\"):
            self.res = max(addition, self.res)
            return
        temp = grid[i][j]
        grid[i][j] = \"#\"
        self.dfs(i+1, j, addition+temp, grid)
        self.dfs(i-1, j, addition+temp, grid)
        self.dfs(i, j+1, addition+temp, grid)
        self.dfs(i, j-1, addition+temp, grid)
        grid[i][j] = temp
        
            
            
