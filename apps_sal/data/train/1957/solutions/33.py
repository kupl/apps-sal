from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
      if len(grid) == 1 and len(grid[0]) == 1:
        return 0
      queue = deque([(0,0,k,0)])#i,j,free eliminate chance, steps
      directions = [[0,1], [0,-1], [-1,0], [1,0]]
      visited = set([(0,0,k)])
    
      M, N = len(grid), len(grid[0])
      while queue:
        i, j, m, steps = queue.popleft()
        for dx, dy in directions:
          x = dx + i
          y = dy + j
          if 0 <= x < M and 0 <= y < N:
            if grid[x][y] == 1 and m > 0 and (x, y, m-1) not in visited:
              visited.add((x,y,m-1))
              queue.append((x, y, m-1, steps+1))
              
            if grid[x][y] == 0 and  (x, y, m) not in visited:
              if x == M-1 and y == N-1:
                return steps + 1
              
              visited.add((x, y, m))
              queue.append((x, y, m, steps+1))
      return -1
          
      

