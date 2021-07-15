from collections import deque 

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid: 
            return -1 
        rows = len(grid)
        cols = len(grid[0])
        visited = {(0, 0, 0)}
        
        queue = deque()
        queue.append((0, 0, 0))
        steps = 0
        
        while queue: 
            newqueue = deque()
            for (x, y, r) in queue: 
                if x == rows - 1 and y == cols - 1:
                    return steps
                for (i, j) in [(x, y - 1), (x, y+1), (x+1, y), (x-1, y)]:
                    if i >= 0 and i < rows and j >= 0 and  j < cols: 
                        if grid[i][j] == 0 and (i, j, r) not in visited:
                            newqueue.append((i, j, r))
                            visited.add((i, j, r))
                        elif grid[i][j] == 1 and r+1 <= k and (i, j, r+1) not in visited: 
                            newqueue.append((i, j, r+1))
                            visited.add((i, j, r+1))
            queue = newqueue
            steps += 1
        return -1 
            
#         if not grid:
#             return -1
#         rows = len(grid)
#         cols = len(grid[0])
        
#         #dist = grid.copy()
#         #dist[0][0] = 0
#         dist = [[0 for j in range(cols)] for i in range(rows)]
#         queue = deque() 
#         queue.append((0, 0, 0))
#         #queue = [(0, 0, 0)]
#         while queue:
#             (x, y, r) = queue.popleft()
            
#             if y > 0 and grid[x][y-1] >= 0:
#                 if grid[x][y-1] == 0:
#                     queue.append((x, y-1, r))
#                     dist[x][y-1] = dist[x][y] + 1
#                 if grid[x][y-1] == 1 and r+1 <= k:
#                     queue.append((x, y-1, r + 1))
#                     dist[x][y-1] = dist[x][y] + 1
#             if x > 0 and grid[x-1][y] >= 0:
#                 if grid[x-1][y] == 0:
#                     queue.append((x-1, y, r))
#                     dist[x-1][y] = dist[x][y] + 1
#                 if grid[x-1][y] == 1 and r+1 <= k:
#                     queue.append((x-1, y, r + 1))
#                     dist[x-1][y] = dist[x][y] + 1
#             if x < rows -1 and grid[x+1][y] >= 0:
#                 if grid[x+1][y] == 0:
#                     queue.append((x+1, y, r))
#                     dist[x+1][y] = dist[x][y] + 1
#                 if grid[x+1][y] == 1 and r+1 <= k:
#                     queue.append((x+1, y, r + 1))
#                     dist[x+1][y] = dist[x][y] + 1
#             if y < cols-1 and grid[x][y+1] >= 0:
#                 if grid[x][y+1] == 0:
#                     queue.append((x, y+1, r))
#                     dist[x][y+1] = dist[x][y] + 1
#                 if grid[x][y+1] == 1 and r+1 <= k:
#                     queue.append((x, y+1, r + 1))
#                     dist[x][y+1] = dist[x][y] + 1
#             grid[x][y] = -1
#         print(dist)
#         if grid[rows-1][cols-1] != -1: 
#             return -1
#         else:
#             return dist[rows-1][cols-1]

