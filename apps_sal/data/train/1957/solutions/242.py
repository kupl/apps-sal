from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # we have shortest path in unweighted graph, so we use bfs
        # we store obstacles here and remove if we can until we reach to end
        if not grid:
            return 0
        
        queue = deque()
        visited = dict()
        if grid[0][0] == 1:
            queue.append((0, 0, k-1, 0))
            visited[0, 0] = k-1
        else:
            queue.append((0, 0, k, 0))
            visited[0, 0] = k
        
        n, m = len(grid), len(grid[0])
        while queue:
            x, y, obst, path = queue.popleft()
            if obst < 0:
                continue
            if x == n-1 and y == m-1:
                if grid[x][y] == 0 or (grid[x][y] == 1 and obst >= 1): # if end is an obstacle, check if we can accept it
                    return path
                # we can keep going to check for another path
            
            for x_path, y_path in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
                # continue if out of bounds OR number of obstacles to this point earlier is higher, then we prune
                if x_path < 0 or y_path < 0 or x_path >= n or y_path >= m or \\
                ((x_path, y_path) in visited and visited[(x_path, y_path)] >= obst) \\
                or (grid[x_path][y_path] == 1 and obst == 0):
                    continue
                
                if grid[x_path][y_path] == 1:
                    visited[(x_path, y_path)] = obst-1
                    queue.append((x_path, y_path, obst-1, path+1))
                else:
                    visited[(x_path, y_path)] = obst
                    queue.append((x_path, y_path, obst, path+1))
        return -1
                                                                              
                    
                
            
        
        
