class Solution:
    def __init__(self):
        self.EMPTY = 0
        self.DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.EMPTY:
                    continue
                    
                max_gold = max(max_gold, self.dfs(grid, i, j, set()))
                
        return max_gold
    
    def dfs(self, grid, x, y, visited):
        if not self.inbound(grid, x, y) or (x, y) in visited or grid[x][y] == self.EMPTY:
            return 0
        
        visited.add((x, y))
        gold = 0
        
        for delta_x, delta_y in self.DIR:
            next_x, next_y = x + delta_x, y + delta_y
            
            gold = max(gold, self.dfs(grid, next_x, next_y, visited))
        
        gold += grid[x][y]
        visited.discard((x, y))
        return gold
        
    def inbound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
