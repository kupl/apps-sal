class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return 0
        
        queue = collections.deque([(0,0,k,0)])
        r, c = len(grid), len(grid[0])
        
        visited = set()
        direction = []
        while queue:
            x, y, eliminate, steps = queue.popleft()
            if x == r-1 and y == c-1:
                return steps
            for nx, ny in (x+1, y), (x-1, y), (x, y-1), (x, y+1):
                if nx >= 0 and nx < r and ny >= 0 and ny < c:
                    if eliminate > 0 and (nx, ny, eliminate-1) not in visited and grid[nx][ny] == 1:
                        queue.append((nx, ny, eliminate-1, steps+1))
                        visited.add((nx, ny, eliminate-1))
                    if (nx, ny, eliminate) not in visited and grid[nx][ny] == 0:
                        queue.append((nx, ny, eliminate, steps+1))
                        visited.add((nx, ny, eliminate))

                    
        return -1

