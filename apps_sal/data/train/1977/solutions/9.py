class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # find connected 0s not touching any border
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        ans = 0
        
        def dfs(i,j,val):
            if 0<=i<m and 0<=j<n and grid[i][j]==0:
                grid[i][j] = val
                dfs(i, j+1, val)
                dfs(i+1, j, val)
                dfs(i-1, j, val)
                dfs(i, j-1, val)

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    dfs(i, j, 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 1)
                    ans+=1
                    
        return ans
                
        

