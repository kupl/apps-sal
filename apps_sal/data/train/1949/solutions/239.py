class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.max_gold = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                visited = set()
                self.dfs(grid, 0, row, col, visited)
                
        return self.max_gold
    
    def dfs(self,grid, curr_gold, i, j, visited):
    #base case
        if (i,j) in visited or not (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])) or grid[i][j] == 0: 
            if self.max_gold < curr_gold:
                self.max_gold = curr_gold
            return 
        visited.add((i,j))
        self.dfs(grid, curr_gold + grid[i][j] ,i+1, j, visited)
        visited.discard((i,j))
        visited.add((i,j))
        self.dfs(grid, curr_gold + grid[i][j], i-1, j, visited)
        visited.discard((i,j))
        visited.add((i,j))
        self.dfs(grid, curr_gold + grid[i][j] , i, j-1, visited)
        visited.discard((i,j))
        visited.add((i,j))
        self.dfs(grid, curr_gold + grid[i][j] , i, j+1, visited)
        visited.discard((i,j))
        return
    
        
            
        

