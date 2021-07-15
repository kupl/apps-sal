class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.gold = 0
        
        def DFS(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            
            tmp = grid[i][j]
            grid[i][j] = 0
            self.gold = max(tmp + DFS(i+1, j), tmp + DFS(i-1, j), tmp + DFS(i, j+1), tmp + DFS(i, j-1))
            grid[i][j] = tmp
            return self.gold

        
        res = 0
        for i in range(m):
            for j in range(n):
                self.gold = 0
                res = max(res, DFS(i, j))
        return res
