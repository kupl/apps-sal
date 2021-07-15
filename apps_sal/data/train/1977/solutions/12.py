from functools import lru_cache
class Solution:
    def closedIsland(self, grid):
        n=len(grid)
        m=len(grid[0])
        @lru_cache(None)
        def dfs(x,y):
            if x==0 or y==0 or x==n-1 or y==m-1 or grid[x][y]!=0:
                return grid[x][y]!=0
            t=True
            grid[x][y]=-1
            t=dfs(x-1,y) & dfs(x+1,y) & dfs(x,y+1) & dfs(x,y-1)
            return t
        res=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    res+=dfs(i,j)
        return res
