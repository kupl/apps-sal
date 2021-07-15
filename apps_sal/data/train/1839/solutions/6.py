class Solution:
     def swimInWater(self, grid):
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         m, n = len(grid), len(grid[0])
         seen = set()
         seen.add((0, 0))
         heap = [(grid[0][0], 0, 0)]
         ans = 0
         while heap:
             h, i, j = heapq.heappop(heap)
             ans = max(ans, h)
             if i == m-1 and j == n-1:
                 return ans
             for a, b in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                 if 0 <= a < m and 0 <= b < n and (a, b) not in seen:
                     heapq.heappush(heap, (grid[a][b], a, b))
                     seen.add((a, b))

