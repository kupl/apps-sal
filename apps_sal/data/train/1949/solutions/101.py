DIRS = [(-1,0),(1,0),(0,-1),(0,1)]
class Solution:
    def getMaximumGold(self, grid):
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, seen):
            if i >= m or i < 0 or j >= n or j < 0 or (i,j) in seen or grid[i][j] == 0:
                return 0
            gold = 0
            seen.add((i,j))
            for i_inc, j_inc in DIRS:
                ni, nj = i+i_inc, j+j_inc
                gold = max(gold, dfs(ni, nj, seen))
            seen.remove((i,j))
            return gold + grid[i][j]
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, set()))
        return res
            
        

