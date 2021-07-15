best = 0
            
def collect(grid, r, c, curr):
    if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] != 0:
        nonlocal best
        val = grid[r][c]
        curr += val
        best = max(best, curr)
        
        temp = grid[r][c]
        grid[r][c] = 0
        
        collect(grid, r + 1, c, curr)        
        collect(grid, r - 1, c, curr)
        collect(grid, r, c + 1, curr)
        collect(grid, r, c - 1, curr)
        curr -= val
        
        grid[r][c] = val
        
        

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        nonlocal best
        best = 0
        rows = len(grid)
        cols = len(grid[0])        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    collect(grid, r, c, 0)
        return best                    

