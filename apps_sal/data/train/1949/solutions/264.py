class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold =0
        m, n = len(grid), len(grid[0])
        
        def get_max(i, j):
            if i<0 or i >= m or j<0 or j>= n or grid[i][j] ==0:
                return 0
            tmp = grid[i][j]
            max_gold = 0 
            grid[i][j] = 0
            max_gold = max(max_gold, get_max(i+1, j), get_max(i-1, j),get_max(i, j+1) ,get_max(i, j-1))
            grid[i][j] = tmp
            return max_gold + tmp
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] !=0:
                    max_gold  = max(max_gold, get_max(i,j,))
        return max_gold
                    
            
            
            

