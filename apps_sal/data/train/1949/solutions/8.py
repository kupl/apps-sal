class Solution:
    gold = 0
    def dfs(self,grid,i,j,current):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
            return
        current += grid[i][j]
        temp = grid[i][j]
        grid[i][j] = 0
        self.dfs(grid,i,j-1,current)
        self.dfs(grid,i,j+1,current)
        self.dfs(grid,i+1,j,current)
        self.dfs(grid,i-1,j,current)
        grid[i][j] = temp
        self.gold = max(self.gold,current)
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    current = 0
                    self.dfs(grid,i,j,current)
        return self.gold
