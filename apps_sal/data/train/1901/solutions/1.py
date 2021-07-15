class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        borders = dict()
        seen = set()
        max_size = 0
        
        def bfs(r, c):
            nonlocal max_size
            size = 1
            border = set()
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for r, c in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
                    if 0 <= r < n_rows and 0 <= c < n_cols and (r,c) not in seen:
                        
                        if grid[r][c] == 1:
                            size += 1
                            stack.append((r, c))
                            seen.add((r, c))
                        else:
                            border.add((r, c))
            
            max_size = max(max_size, size)
            for r, c in border:
                if (r, c) in borders:
                    max_size = max(max_size, borders[(r, c)] + size)
                    borders[(r, c)] = borders[(r, c)] + size
                else:
                    borders[(r, c)] = size
            
            
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    bfs(r, c)
                    
        return max_size + 1 if max_size != n_rows*n_cols else max_size
