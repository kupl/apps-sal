class Solution:
     def swimInWater(self, grid):
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         n = len(grid)
         flag = []
         for i in range(n):
             flag.append([0] * n)
         flag[0][0] = 1
         pos = [0] * (n * n)
         for i in range(n):
             for j in range(n):
                 pos[grid[i][j]] = (i, j)
 
                 
         def search(x, y, n, grid, flag, k):
             if x < 0 or x >= n or y < 0 or y >= n or flag[x][y] == 2:
                 return
             if grid[x][y] > k:
                 flag[x][y] = 1
             else:
                 flag[x][y] = 2
                 search(x - 1, y, n, grid, flag, k)
                 search(x + 1, y, n, grid, flag, k)
                 search(x, y - 1, n, grid, flag, k)
                 search(x, y + 1, n, grid, flag, k)
         for k in range(n * n):
             x, y = pos[k]
             if flag[x][y] == 1:
                 search(x, y, n, grid, flag, k)
             if flag[n - 1][n - 1] == 2:
                 return k

