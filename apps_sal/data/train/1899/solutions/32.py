class Solution:
    def shortestBridge1(self, grid: List[List[int]]) -> int:
        \"\"\"
        # loop to find first 1 in one of the 2 islands
        # dfs from first 1 and mask all 1 to -1 in this island and collect boundry as well
        # From boundries of first island, bfs until find 1 which must be part of 2nd island
        \"\"\"
        
        def moves(row, col):
            for rm, cm in (0, 1), (1, 0), (0, -1), (-1, 0):
                nr, nc = row + rm, col + cm
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc
        
        def get_first() -> Tuple[int, int]:
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c]:
                        return r, c
        
        def update_boundaries_dfs_rec(row, col):
            grid[row][col] = -1
            for nr, nc in moves(row, col):
                if not grid[nr][nc]:
                    boundary_set.add((row, col))
                if  grid[nr][nc] == 1:
                    update_boundaries_dfs_rec(nr, nc)
        
        rows, cols = len(grid), len(grid[0])
        # bfs to find short distance
        boundary_set = set()
        update_boundaries_dfs_rec(*get_first())
        step = 0
        while boundary_set:
            next_boundary_set = set()
            for r, c in boundary_set:
                for nr, nc in moves(r, c):
                    if grid[nr][nc] == 1:
                        return step
                    if grid[nr][nc]:
                        continue
                    grid[nr][nc] == -1
                    next_boundary_set.add((nr, nc))
            step += 1
            boundary_set = next_boundary_set
            
    def shortestBridge(self, A):
        def dfs(i, j):
            A[i][j] = -1
            bfs.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)
                    
        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j
                    
        n, step, bfs = len(A), 0, []
        dfs(*first())
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        # if A[x][y] == -1:
                        #     continue
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            bfs = new
                
                
                
                
                
            
        
