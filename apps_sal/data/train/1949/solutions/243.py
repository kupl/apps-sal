class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def fun(g,i,j):
            if i<0 or i>=m or j<0 or j>=n or g[i][j]==0:
                return 0
            t=g[i][j]
            g[i][j]=0
            curr=t+max(fun(g,i-1,j),fun(g,i,j-1),fun(g,i+1,j),fun(g,i,j+1))
            g[i][j]=t
            return curr
        ml=0
        for i in range(m):
            for j in range(n):
                    ml=max(ml,fun(grid,i,j))
        return ml

