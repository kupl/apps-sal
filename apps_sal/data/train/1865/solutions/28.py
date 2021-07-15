class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        def connected(s, e):
            q = collections.deque([s])
            visited = set([s])
            while q:
                r, c = q.popleft()
                if (r, c) == e: return True
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '.':
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return False
        
        B = S = T = (0, 0)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'B': 
                    B = (r, c)
                    grid[r][c] = '.'
                elif grid[r][c] == 'S': 
                    S = (r, c)
                    grid[r][c] = '.'
                elif grid[r][c] == 'T': 
                    T = (r, c)
                    grid[r][c] = '.'
                    
        ans = 0
        q = collections.deque([(B, S, 0)])
        visited = set([(B, S)])
        while q:
            (r, c), (rs, cs), step = q.popleft()
            if (r, c) == T: return step
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                pr, pc = r-dr, c-dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '.' and ((nr, nc), (r, c)) not in visited:
                    grid[r][c] = 'B'
                    if 0 <= pr < m and 0 <= pc < n and grid[pr][pc] == '.' and connected((pr, pc), (rs, cs)):
                        visited.add(((nr, nc), (r, c)))
                        q.append(((nr, nc), (r, c), step+1))
                    grid[r][c] = '.'
        return -1
                        
            
                    
            

