class Solution:
     def swimInWater(self, grid):
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         n = len(grid)
         pq = [(grid[0][0], 0, 0)]
         seen = set([(0, 0)])
         res = 0
         while True:
             val, y, x = heapq.heappop(pq)
             res = max(res, val)
             if y == x == n - 1:
                 return res
             for i, j in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                 if 0 <= i < n and 0 <= j < n and (i, j) not in seen:
                     seen.add((i, j))
                     heapq.heappush(pq, (grid[i][j], i, j))
         return 0

