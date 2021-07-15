class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(x,y):  #由(x,y)出发可取的数目
            if x<0 or x>=m or y<0 or y>=n or grid[x][y]==0:
                return 0
            t=grid[x][y]
            grid[x][y]=0
            s=t+max(dfs(x+1,y),dfs(x-1,y),dfs(x,y+1),dfs(x,y-1))
            grid[x][y]=t
            return s
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res=max(res,dfs(i,j))
        return res
