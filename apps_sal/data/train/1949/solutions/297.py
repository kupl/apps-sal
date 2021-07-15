class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        seen = set()
        n,m = len(grid),len(grid[0])
        self.ans = 0
        def dfs(r,c,cur = 0):
            seen.add((r,c))
            cur += grid[r][c]
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                x,y = r + dx, c + dy
                if 0 <= x < n and 0 <= y < m and (x,y) not in seen and grid[x][y] != 0:
                    dfs(x,y,cur)
            seen.remove((r,c))
            self.ans = max(self.ans, cur)
        
        for i in range(n):
            for j in range(m):
                if (i,j) not in seen and grid[i][j] != 0:
                    dfs(i,j)
                    
        return self.ans
