class Solution:
    # DFS failed
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        cache = {}
        visited = set()
        def dp(b, p):
            if not (0<=b[0]<m and 0<=b[1]<n and 0<=p[0]<m and 0<=p[1]<n) or grid[b[0]][b[1]] == '#' or grid[p[0]][p[1]] == '#' or b == p:
                return float(\"inf\")
            if grid[b[0]][b[1]] == 'T':
                return 0
            if (b, p) in cache:
                return cache[(b, p)]
            if (b, p) in visited:
                return float(\"inf\")
            visited.add((b, p))
            ans = float(\"inf\")
            if abs(b[0] - p[0]) + abs(b[1] - p[1]) == 1:
                delta = (b[0] - p[0], b[1] - p[1])
                ans = 1+dp((b[0]+delta[0], b[1]+delta[1]), b)
            ans = min(ans, min(dp(b, pp) for pp in ((p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1))))
            visited.remove((b, p))
            cache[(b, p)] = ans
            return ans
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    b = (i, j)
                if grid[i][j] == 'S':
                    p = (i, j)
        ans = dp(b, p)
        print(cache)
        return -1 if ans == float(\"inf\") else ans
    
    # BFS
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        q = collections.deque()
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    b = (i, j)
                if grid[i][j] == 'S':
                    p = (i, j)
                    
        q.append((b, p, 0))
        visited.add((b, p))
        while q:
            b, p, c = q.popleft()
            if grid[b[0]][b[1]] == 'T':
                return c
            for pp in ((p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1)):
                if (b, pp) not in visited and 0<=pp[0]<m and 0<=pp[1]<n and grid[pp[0]][pp[1]] != '#' and b != pp:
                    q.appendleft((b, pp, c))
                    visited.add((b, pp))
            if abs(b[0] - p[0]) + abs(b[1] - p[1]) == 1:
                delta = (b[0] - p[0], b[1] - p[1])
                p = b
                b = (b[0]+delta[0], b[1]+delta[1])
                if (b, p) not in visited and 0<=b[0]<m and 0<=b[1]<n and grid[b[0]][b[1]] != '#':
                    q.append((b, p, c+1))
                    visited.add((b, p))
        return -1
    
    # BFS + A*
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        from heapq import heappop, heappush
        
        q = []
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    b = (i, j)
                if grid[i][j] == 'S':
                    p = (i, j)
                if grid[i][j] == 'T':
                    t = (i, j)
                
                    
        q.append((abs(t[0]-b[0]) + abs(t[1]-b[1]), 0, b, p))
        visited.add((b, p))
        while q:
            gh, g, b, p = heappop(q)
            if b == t:
                return g
            for pp in ((p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1)):
                if (b, pp) not in visited and 0<=pp[0]<m and 0<=pp[1]<n and grid[pp[0]][pp[1]] != '#' and b != pp:
                    heappush(q, (gh, g, b, pp))
                    visited.add((b, pp))
            if abs(b[0] - p[0]) + abs(b[1] - p[1]) == 1:
                delta = (b[0] - p[0], b[1] - p[1])
                p = b
                b = (b[0]+delta[0], b[1]+delta[1])
                if (b, p) not in visited and 0<=b[0]<m and 0<=b[1]<n and grid[b[0]][b[1]] != '#':
                    heappush(q, (g+1+abs(t[0]-b[0]) + abs(t[1]-b[1]), g+1, b, p))
                    visited.add((b, p))
        return -1
            
            
