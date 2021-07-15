class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        self.ans = 0
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == 0:
                return 0
            
            visited[i][j] = True
            res = grid[i][j] + max(dfs(i-1, j), dfs(i+1, j), dfs(i, j-1), dfs(i, j+1))
            visited[i][j] = False
            self.ans = max(self.ans, res)
            return res
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
        
        return self.ans

