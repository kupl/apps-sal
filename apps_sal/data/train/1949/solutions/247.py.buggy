class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def find_gold(grid, i, j, r, c, traversed):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == 0 or f\"{i}-{j}\" in traversed:
                return 0
            
            return grid[i][j] + max(
                    find_gold(grid, i + 1, j, r, c, traversed + [f\"{i}-{j}\"]), 
                    find_gold(grid, i - 1, j, r, c, traversed + [f\"{i}-{j}\"]), 
                    find_gold(grid, i, j + 1, r, c, traversed + [f\"{i}-{j}\"]), 
                    find_gold(grid, i, j - 1, r, c, traversed + [f\"{i}-{j}\"]))
        
        r = len(grid)
        c = len(grid[0])
        
        maxi = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    traversed = []
                    maxi = max(maxi, find_gold(grid, i, j, r, c, traversed))
        return maxi
        
