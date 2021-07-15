class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        queue = deque()
        queue.append(((0, 0, 0, 0)))
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited = set([(0, 0 , 0)])

        
        while queue:
            x, y, elim, path = queue.popleft()
            if x==m-1 and y==n-1: return path
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n:
                    if grid[nx][ny] == 0 and (nx, ny, elim) not in visited:
                        queue.append((nx, ny, elim, path + 1))
                        visited.add((nx,ny, elim))
                    if grid[nx][ny] == 1 and elim<k and (nx, ny, elim-1) not in visited:
                        queue.append((nx, ny, elim+1, path + 1))
                        visited.add((nx,ny, elim+1))
        return -1
