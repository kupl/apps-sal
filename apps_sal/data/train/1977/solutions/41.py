from collections import deque

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.m, self.n = m, n
        visited = [[False]*n for _ in range(m)]
        Q = deque()
        count = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] or (grid[i][j] == 1):
                    continue
                visited[i][j] = True
                Q.append((i,j))
                edge_found = False
                while len(Q) > 0:
                    x,y = Q.popleft()
                    #print(x,y)
                    if self.is_edge(x, y):
                        edge_found = True
                    for p,q in self.nbrs(x, y):
                        if (not visited[p][q]) and (grid[p][q] == 0):
                            #print('adding ', p, q)
                            visited[p][q] = True
                            Q.append((p,q))
                if not edge_found:
                    count += 1
        return count
                            
    def is_edge(self, i, j):
        return (i == 0) or (i == self.m - 1) or (j == 0) or (j == self.n - 1)
                    
    def nbrs(self, i, j):
        for d in (-1, 1):
            if (0 <= i + d < self.m):
                yield (i + d, j)
            if (0 <= j + d < self.n):
                yield (i, j + d)

