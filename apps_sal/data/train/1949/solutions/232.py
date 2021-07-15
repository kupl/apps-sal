class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = 0
        M = len(grid)
        N = len(grid[0])
        cords = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        def recur(x, y):
            if x < 0 or x >= M or y < 0 or y >= N or grid[x][y] == 0:
                return 0
            temp = grid[x][y]
            grid[x][y] = 0
            total = 0
            for dx, dy in cords:
                dx += x
                dy += y
                total = max(total, recur(dx, dy))
            grid[x][y] = temp
            return total + temp 
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 0:
                    res = max(recur(i, j), res)
        return res
