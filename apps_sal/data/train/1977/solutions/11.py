class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,grid):
            if grid[i][j]==1:
                return True
            if i<=0 or j<=0 or i>=n-1 or j>=m-1:
                return False
            grid[i][j]=1
            
            up=dfs(i+1,j,grid)
            down=dfs(i-1,j,grid)
            right=dfs(i,j+1,grid)
            left=dfs(i,j-1,grid)
            
            return up and down and right and left
        
        cnt=0
        n=len(grid)
        m=len(grid[0])
        for i in range(1,n-1):
            for j in range(1,m-1):
                if grid[i][j]==0 and dfs(i,j,grid):
                    cnt+=1
        return cnt

