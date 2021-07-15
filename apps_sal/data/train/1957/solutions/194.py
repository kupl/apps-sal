class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:        
        if not len(grid) or not len(grid[0]):
            return -1
        
        seen = set()
        m = len(grid)
        n = len(grid[0])
        
        def validMove(x, y):
            return x >= 0 and y >= 0 and x < m and y < n and (x,y) not in seen
        
        q = [(0, 0, 0, 0)]
        
        while q:
            x, y, z, obs = q.pop(0)
            if x == m-1 and y == n-1:
                return z
                
            if (x, y, obs) in seen:
                continue
                
            seen.add((x, y, obs))
            if grid[x][y] == 1 and obs == k:
                continue
            obs += grid[x][y] == 1
                
            dirs = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            
            for d in dirs:
                if validMove(*d):
                    a, b = d
                    q.append((d[0], d[1], z+1, obs))
        
        return -1

