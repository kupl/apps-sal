from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        if m == n == 1: return 0
        
        
        memo = [[-1] * n for _ in range(m)]
        queue = deque()
        queue.append( (0, 0, k, 0) )
        visited = set()
        visited.add((0,0,k))
        while queue:
            x, y, rem, res = queue.popleft()
            if rem < 0:
                continue
            
            for i, j in ( (x+1, y), (x-1, y), (x, y-1), (x, y+1) ):
                
                if 0 <= i < m and 0 <= j < n and (i, j, rem) not in visited: 
                    if i == m-1 and j == n-1:
                        return res + 1
                    visited.add((i, j, rem))
                    if grid[i][j] == 0:
                        queue.append( (i, j, rem, res+1) )
                    else:
                        queue.append( (i, j, rem-1, res+1) )
        
        return -1
        

