class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        greatest = 0
        
        starts = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    q = collections.deque([])
                    q.append((row, col, [(row, col)], grid[row][col]))
                    maxx = 0
                    while q:
                        r, c, path, total = q.popleft()
                        maxx = max(maxx, total)
                        for y, x in directions:
                            nr = r + y
                            nc = c + x
                            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and \\
                               grid[nr][nc] != 0 and (nr, nc) not in path:
                                q.append((nr, nc, path + [(nr, nc)], total + grid[nr][nc]))

                    greatest = max(maxx, greatest)
        return greatest
#         if not grid:
#             return 0
        
#         rows = len(grid)
#         cols = len(grid[0])
#         m = -float('inf')
        
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] !=0:
#                     p = self.dfs(i, j, rows, cols, grid)
#                     m = max(m, p)
                    
#         return m            
    
#     def dfs(self, i, j, rows, cols, grid):
#         if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
#             return 0
        
#         c = grid[i][j]
#         grid[i][j] = 0
        
#         l = self.dfs(i, j - 1, rows, cols, grid)
#         r = self.dfs(i, j + 1, rows, cols, grid)
#         u = self.dfs(i + 1, j, rows, cols, grid)
#         d = self.dfs(i - 1, j, rows, cols, grid)
        
#         grid[i][j] = c
        
#         return max(l, r, u, d) + c
        
