class Solution:
    def dfs(self, i, j, gold):
        flag = True
        
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0<=ni<self.m and 0<=nj<self.n and self.grid[ni][nj]>0:
                tmp = self.grid[i][j]
                self.grid[i][j] = 0
                self.dfs(ni, nj, gold+self.grid[ni][nj])
                self.grid[i][j] = tmp
                flag = False
        
        if flag:
            self.ans = max(self.ans, gold)
        
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.ans = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]>0:
                    self.dfs(i, j, grid[i][j])
        
        return self.ans
        

