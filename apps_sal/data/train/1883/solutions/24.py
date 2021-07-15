class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(i,j,N):
            if N==-1 and grid[i][j]==2: return 1
            grid[i][j]=-1                    
            res = sum([dfs(row,col,N-1) for x,y in dirs for row,col in [(i+x,j+y)] if 0<=row<m and 0<=col<n and (N>0 and not grid[row][col] or N==0 and grid[row][col]==2)])
            grid[i][j]=0
            return res
            
        m,n = len(grid),len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        N = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: start=[i,j]
                elif not grid[i][j]: N+=1
        return dfs(start[0],start[1],N)
