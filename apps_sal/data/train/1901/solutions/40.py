class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        M, N = len(grid), len(grid[0])
        size = [0, 0]
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    num = self.dfs(grid, i, j, len(size))
                    size.append(num)
                    
        #print(size)
        res = 0            
        for x0 in range(M):
            for y0 in range(N):
                if grid[x0][y0] == 0:
                    tmpSum = 1
                    tmpClr = set()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        x = x0 + dx
                        y = y0 + dy
                        if 0 <= x < M and 0 <= y < N:
                            tmpClr.add(grid[x][y])

                    for c in tmpClr:
                        tmpSum += size[c]
                        
                    res = max(res, tmpSum)
                      
        return res if res > 0 else M*N
    
    def dfs(self, grid, x0, y0, clr):
        grid[x0][y0] = clr
        res = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = x0 + dx
            y = y0 + dy
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                res += self.dfs(grid, x, y, clr)
                
        return res
                    

