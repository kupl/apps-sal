class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or (not grid[0]):
            return 0
        r, c = len(grid), len(grid[0])
        def dfs(i, j, curr, visited):
            self.mx = max(self.mx, curr)
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                if (0<=i+di<r) and (0<=j+dj<c) and (grid[i+di][j+dj]!=0) and ((i+di,j+dj) not in visited):
                    visited.add((i+di,j+dj))
                    dfs(i+di, j+dj, curr+grid[i+di][j+dj], visited)
                    visited.remove((i+di, j+dj))
            return
        self.mx = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    dfs(i, j, grid[i][j], {(i,j)})
        return self.mx
