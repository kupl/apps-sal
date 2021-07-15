class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        q = collections.deque()
        q.append((0,0,0,0))
        visited = set()
        
        while q:
            r, c, direction, steps = q.popleft()
            
            if (r,c,direction) == (n-1, n-2, 0):
                return steps
            if (r,c, direction) not in visited:
                visited.add((r,c, direction))
                if direction:
                    if c + 1 < n and grid[r][c + 1] + grid[r + 1][c + 1] == 0:
                        q.append((r, c + 1, 1, steps + 1))
                        q.append((r, c, 0, steps + 1))
                    if r + 2 < n and grid[r + 2][c] == 0:
                        q.append((r + 1, c, 1, steps + 1)) 
                else:
                    if r + 1 < n and grid[r + 1][c] + grid[r + 1][c + 1] == 0:
                        q.append((r + 1, c, 0, steps + 1))
                        q.append((r, c, 1, steps + 1))

                    if c + 2 < n and grid[r][c + 2] == 0: 
                        q.append((r, c + 1, 0, steps + 1))

        return -1
                    
                
                

