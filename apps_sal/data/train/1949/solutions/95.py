class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid),len(grid[0])
        
        def getMaximumGold_helper(grid, i, j):
            if i >= nrow or i<0 or j >= ncol or j<0:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            cur = grid[i][j]
            grid[i][j] = 0
            
            res = cur + max(getMaximumGold_helper(grid,i,j+1),
                       getMaximumGold_helper(grid,i,j-1),
                       getMaximumGold_helper(grid,i+1,j),
                       getMaximumGold_helper(grid,i-1,j))
            
            grid[i][j] = cur
            return res
    
        max_gold = 0
        for i in range(nrow):
            for j in range(ncol):
                cur_gold = getMaximumGold_helper(grid, i, j)
                max_gold = max(max_gold,cur_gold)
        return max_gold
            
            

