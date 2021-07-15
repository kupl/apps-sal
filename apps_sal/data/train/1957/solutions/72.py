class Solution:
    \"\"\"
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = collections.deque([(0,0,0)]) # row, col, num of obstacles met so far
        visited = {(0,0): 0}           # row, col   =>   num of obstacles met so far
        steps = 0
        
        while q:
            for _ in range(len(q)):
                i, j, obstacles = q.popleft()
                
                if obstacles > k:
                    continue
                
                if i == len(grid)-1 and j == len(grid[0]) - 1:
                    return steps
                
                neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                
                for x, y in neighbors:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        next_obstacle = obstacles + grid[x][y]
                        
                        if next_obstacle < visited.get((x,y), float(\"inf\")):
                            visited[(x,y)] = next_obstacle
                            q.append((x, y, next_obstacle))
            steps += 1
        return -1
    \"\"\"
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = collections.deque([(0,0,0,0)]) # row, col, obstacles_removed, distance_from_origin
        visited = {(0, 0, 0)}              # row, col, obstacles_removed
        
        while q:
            i, j, obstacles, dist = q.popleft()
            
            if i == len(grid)-1 and j == len(grid[0]) - 1:
                return dist
            
            if obstacles > k:
                continue
            
            neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            
            for x, y in neighbors:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    if (x, y, obstacles + grid[x][y]) not in visited:
                        visited.add((x, y, obstacles + grid[x][y]))
                        q.append((x, y, obstacles + grid[x][y], dist + 1))
                    
                    # if grid[x][y] == 1:
                    #     if obstacles < k and (x, y, obstacles+1) not in visited:
                    #         visited.add((x, y, obstacles+1))
                    #         q.append((x, y, obstacles+1, dist+1))
                    # else:
                    #     if (x, y, obstacles) not in visited:
                    #         visited.add((x, y, obstacles))
                    #         q.append((x, y, obstacles, dist+1))
        return -1

