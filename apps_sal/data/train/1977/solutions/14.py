class UnionFind:
    
    def __init__(self):
        self.parents = {}
        
    def find(self, a):
        if a in self.parents:
            while a != self.parents[a]:
                a = self.parents[a]
        else:
            self.parents[a] = a
        return self.parents[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a > b: a, b = b, a # always use smaller key
        self.parents[b] = a

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # union find
        m, n = len(grid), len(grid[0])
        uf = UnionFind()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if i == 0 or i == m-1 or j == 0 or j == n-1:
                        uf.union((-1,-1), (i,j)) # use (-1,-1) to be edge
                    if i > 0 and grid[i-1][j] == 0:
                        uf.union((i-1,j), (i,j))
                    if j > 0 and grid[i][j-1] == 0:
                        uf.union((i,j-1), (i,j))
                        
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    tup = uf.find((i,j))
                    if tup != (-1,-1):
                        islands.add(tup)
                    
        # print(islands)
        return len(islands)
