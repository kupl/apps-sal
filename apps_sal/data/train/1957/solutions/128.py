class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        if r == 1 and c == 1:
            return 0
        q = deque([(0, 0, 0, 0)])    # row, col, num of obstables met, steps 
        visited = set((0, 0, 0))
        
        while q:
            row, col, met, step = q.popleft()
            if met > k:
                continue
            if row == r-1 and col == c-1:
                return step
            for nr, nc in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                if 0 <= nr < r and 0 <= nc < c:
                    if grid[nr][nc] == 1 and met+1 <= k and (nr, nc, met+1) not in visited:
                        visited.add((nr, nc, met+1))
                        q.append((nr, nc, met+1, step+1))
                    if grid[nr][nc] == 0 and met <= k and (nr, nc, met) not in visited:
                        visited.add((nr, nc, met))
                        q.append((nr, nc, met, step+1))
        
        return -1
