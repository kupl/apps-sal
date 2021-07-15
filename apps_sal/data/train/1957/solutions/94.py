from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # implies start == end
        if m == 1 and n == 1:
            return 0
        
        parent = {}
        start = (0, 0, k)
        goal = (m - 1, n - 1)
        parent[start] = None
        
        k_left = -1
        frontier = deque([start])
        while len(frontier) > 0:
            x, y, z = frontier.popleft()
            if (goal[0], goal[1], k_left) in parent:
                break
            
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if min(i, j) < 0 or i >= m or j >= n:
                    continue
                
                if grid[i][j] == 0 and (i, j, z) not in parent:
                    parent[(i, j, z)] = (x, y, z) 
                    frontier.append((i, j, z))
                    if (i, j) == goal:
                        k_left = z
                        break

                elif grid[i][j] == 1 and z > 0 and (i, j, z-1) not in parent:
                    parent[(i, j, z-1)] = (x, y, z)
                    frontier.append((i, j, z-1))
                    if (i, j) == goal:
                        k_left = z-1
                        break
        
        current = (goal[0], goal[1], k_left)
        steps = 0
        if current not in parent:
            return -1
        while parent[current] is not None:
            steps += 1
            current = parent[current]
        return steps
                
            

