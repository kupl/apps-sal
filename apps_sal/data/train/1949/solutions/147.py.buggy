class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        greatest = 0
        
        starts = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    q = collections.deque([])
                    q.append((row, col, [(row, col)], grid[row][col]))
                    maxx = 0
                    while q:
                        r, c, path, total = q.popleft()
                        maxx = max(maxx, total)
                        for y, x in directions:
                            nr = r + y
                            nc = c + x
                            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and \\
                               grid[nr][nc] != 0 and (nr, nc) not in path:
                                q.append((nr, nc, path + [(nr, nc)], total + grid[nr][nc]))

                    greatest = max(maxx, greatest)
        return greatest
