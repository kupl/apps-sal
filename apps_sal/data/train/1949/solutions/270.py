class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        self.res = 0
                
        def dfs(grid, i, j, cur):
            nbr = [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]
            temp = grid[i][j]
            self.res = max(self.res, cur + temp)
    
            for r, c in nbr:
                if 0 <= r < M and 0 <= c < N and grid[r][c]:
                    grid[i][j] = 0
                   
                    dfs(grid, r, c, cur + temp)
                    grid[i][j] = temp
    
                    
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    dfs(grid, i, j, 0)
        # dfs(grid, 0, 1, 0)
        print(('res = ', self.res))
        
        return self.res
                    

