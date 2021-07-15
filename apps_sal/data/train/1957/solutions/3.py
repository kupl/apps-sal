from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid[0])
        n = len(grid)
        seen = set()
        queue = deque([(0,0,0,k)])
        while queue:
            x, y, total, r = queue.popleft()
            if x == m-1 and y == n-1:
                return total
            
            if x-1 >= 0 and (x-1, y, r) not in seen:
                seen.add((x-1,y,r))
                if grid[y][x-1] == 0:
                    queue.append((x-1, y, total+1, r))
                if grid[y][x-1] == 1 and r > 0:
                    queue.append((x-1, y, total+1, r-1))

            if x+1 < m and (x+1, y, r) not in seen:
                seen.add((x+1,y,r))
                if grid[y][x+1] == 0:
                    queue.append((x+1, y, total+1, r))
                if grid[y][x+1] == 1 and r > 0:
                    queue.append((x+1, y, total+1, r-1))
            
            if y-1 >= 0 and (x, y-1, r) not in seen:
                seen.add((x,y-1,r))
                if grid[y-1][x] == 0:
                    queue.append((x, y-1, total+1, r))
                if grid[y-1][x] == 1 and r > 0:
                    queue.append((x, y-1, total+1, r-1))
            
            if y+1 < n and (x, y+1, r) not in seen:
                seen.add((x,y+1,r))
                if grid[y+1][x] == 0:
                    queue.append((x, y+1, total+1, r))
                if grid[y+1][x] == 1 and r > 0:
                    queue.append((x, y+1, total+1, r-1))
                        
        return -1
        

    
        
            
        
            

