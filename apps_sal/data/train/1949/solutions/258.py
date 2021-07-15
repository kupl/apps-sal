class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            if x < 0 or x == m or y < 0 or y == n or grid[x][y] == 0:
                return 0
            val = grid[x][y]
            grid[x][y] = 0
            gain = val + max(dfs(x+1,y), dfs(x-1,y), dfs(x, y-1), dfs(x, y+1))
            grid[x][y] = val
            return gain
        
        gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    gold = max(gold, dfs(i,j))
        
        return gold
            

