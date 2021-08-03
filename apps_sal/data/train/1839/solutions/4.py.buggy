import heapq
 class Solution:
     def swimInWater(self, grid):
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         
         def neighbors(n, x, y):
             neighbors = []
             if 0 <= x+1 < n and 0 <= y < n: neighbors.append((x+1, y))
             if 0 <= x-1 < n and 0 <= y < n: neighbors.append((x-1, y))
             if 0 <= x < n and 0 <= y+1 < n: neighbors.append((x, y+1))
             if 0 <= x < n and 0 <= y-1 < n: neighbors.append((x, y-1))
             return neighbors
                 
             
         
         n = len(grid)
         
         poss = set((0,0))
         pq = [(grid[0][0],0,0)]
         maxx = 0
         while pq:
             elem, x, y = heapq.heappop(pq)
             maxx = max(maxx, elem)
             for newx, newy in neighbors(n, x, y):
                 if newx == n-1 and newy == n-1:
                     return max(maxx, grid[n-1][n-1])
                 if (newx, newy) not in poss:
                     poss.add((newx, newy))
                     # neighborval = grid[newx][newy]
                     # if neighborval <= elem:
                     heapq.heappush(pq, (grid[newx][newy], newx, newy))
             # print(pq)
         return maxx
                     
             
             
         
