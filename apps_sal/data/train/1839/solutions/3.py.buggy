import heapq
 
 class Solution:
     def swimInWater(self, grid):
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         q = [(grid[0][0], (0, 0))]
         n = len(grid)
         grid[0][0] = -1
         
         dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
         
         while q:
             val = heapq.heappop(q)
             i = val[1][0]
             j = val[1][1]
             
             if i == j == n - 1:
                 return val[0]
             
             for d in dirs:
                 x = i + d[0]
                 y = j + d[1]
                 
                 if 0 <= x < n and 0 <= y < n and grid[x][y] != -1:
                     heapq.heappush(q, (max(grid[x][y], val[0]), (x, y)))
                     grid[x][y] = -1
         
         return -1
         
         
                     
                     
                     
         
