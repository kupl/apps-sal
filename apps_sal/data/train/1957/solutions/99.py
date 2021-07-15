import collections

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        # (x, y, steps, remaining k)
        stack = collections.deque([(0, 0, 0, k)])
        visited = set()
        m = len(grid)-1
        n = len(grid[0])-1
        
        while stack:
            curr_x, curr_y, steps, remaining = stack.popleft()
            if curr_x ==m and curr_y ==n:
                return steps
            if (curr_x, curr_y, remaining) in visited:
                continue
            visited.add((curr_x, curr_y, remaining))
            directions = [(0, 1), (0, -1), (1, 0), (-1,0)]
            for i, j in directions:
                next_x = curr_x + i
                next_y = curr_y +j
                if next_x>=0 and next_y>=0 and next_x<=m and next_y <=n:
                    if grid[next_x ][next_y] == 0 and (next_x, next_y, remaining) not in visited:
                        stack.append((next_x, next_y, steps+1, remaining))
                    elif remaining-1>=0 and (next_x, next_y, remaining-1) not in visited:
                        stack.append((next_x ,next_y , steps+1, remaining-1))
        return -1

                
            
            
            
        
    
    

