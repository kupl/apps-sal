
class Solution:
    
    def __init__(self, *args, **kwargs):
        self.visited = set()

    def generate_neighbours(self, grid, i, j, m, n):
        if i > 0:
            yield i-1,j
        if i+1 < n:
            yield i+1,j
        if j > 0:
            yield i,j-1
        if j+1 < m:
            yield i,j+1
    
    def dfs(self, grid, i, j, m, n):
        self.visited.add(f\"{i}-{j}\")
        
        if grid[i][j] == 0:
            return 0

        max_gold = 0
        for x, y in  self.generate_neighbours(grid, i, j, m, n):
            if f\"{x}-{y}\" in self.visited:
                continue
                
            gold_found = self.dfs(grid, x, y, m, n)
            max_gold = max(max_gold, gold_found)
            
        self.visited.remove(f\"{i}-{j}\")
        return grid[i][j] + max_gold
            
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        max_gold = 0
        for i in range(n):
            for j in range(m): 
                self.visited = set()
                gold_found = self.dfs(grid, i, j, m, n,)
                max_gold = max(max_gold, gold_found)
        
        return max_gold
    
    # [1,0,7,0,0,0]
    # [2,0,6,0,1,0]
    # [3,5,6,7,4,2]
    # [4,3,1,0,2,0]
    # [3,0,5,0,20,0]
