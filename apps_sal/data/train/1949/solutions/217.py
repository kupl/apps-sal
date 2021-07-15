class Solution:
    def __init__(self):
        self.EMPTY = 0
        self.DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        max_gold = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not (i, j) in visited:
                    max_gold = max(max_gold, self.dfs(grid, i, j, visited))
                
        return max_gold
    
    def dfs(self, grid, i, j, visited):
        if not self.inbound(grid, i, j) or (i, j) in visited or grid[i][j] == self.EMPTY:
            return 0
        
        visited.add((i, j))
        gold = 0
        
        for delta_i, delta_j in self.DIR:
            gold = max(gold, self.dfs(grid, i + delta_i, j + delta_j, visited))
        
        gold += grid[i][j]
        visited.discard((i, j))
        return gold
    
    def inbound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
