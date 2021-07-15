class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
      
        if not grid or not grid[0]: return 0
        
        self.max_gold = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                self.dfs(grid, row, col, 0)
        
        return self.max_gold
    
    def dfs(self, grid, row, col, gold):
        rows = len(grid)
        cols = len(grid[0])
        
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return
        
        prev_gold = grid[row][col]
        
        grid[row][col] = 0
        
        gold += prev_gold
        self.max_gold = max(self.max_gold, gold)
        
        for drow, dcol in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
            self.dfs(grid, drow, dcol, gold)
            
        grid[row][col] = prev_gold
