class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        cache = {} # The key should be (axis, key)
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            if grid[0][0] == 0:
                return 0
            if grid[0][0] == 1:
                if k >= 1:
                    return 0
                return -1
            
        def get_nexts(i, j, k):
            nxts = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            nxts = [(x, y) for x, y in nxts 
                    if x >= 0 and x < m and y >= 0 and y < n 
                    and (x, y) not in pathnodes]
            
            nxts_steps = []
            for x, y in nxts:
                if grid[x][y] == 0:
                    nxts_steps.append((x, y, k))
                if grid[x][y] and k >= 1:
                    nxts_steps.append((x, y, k - 1))
            return nxts_steps
        
        pathnodes = set()
        #bfs
        roots = [(0, 0, k)]
        d = 0
        includes = set(roots)
        while roots:
            next_level = []
            for root in roots:
                nxts = get_nexts(*root)
                for nxt in nxts:
                    if nxt in includes:
                        continue
                    if nxt[:2] == (m - 1, n - 1):
                        return d + 1
                    next_level.append(nxt)
                    includes.add(nxt)
            roots = next_level
            d += 1
        
        return -1
        
            

