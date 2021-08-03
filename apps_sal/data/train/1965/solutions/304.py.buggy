class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n+1))
        self.ranks = [0] * (n+1)
        self.size = 1
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        xpar, ypar = self.find(x), self.find(y)
        if xpar == ypar:
            # already in same set
            return False
        xrank, yrank = self.ranks[x], self.ranks[y]
        if xrank > yrank:
            self.parents[ypar] = xpar
        elif xrank < yrank:
            self.parents[xpar] = ypar
        else:
            self.parents[xpar] = ypar
            self.ranks[ypar] += 1
        self.size += 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1, uf2, ans = UnionFind(n), UnionFind(n), 0
\t\t
        for t, u, v in edges:
            if t != 3:
                continue
            if not uf1.union(u, v) or not uf2.union(u, v):
                ans += 1
        
        for t, u, v in edges:
            if t == 1 and not uf1.union(u, v):
                ans += 1
            elif t == 2 and not uf2.union(u, v):
                ans += 1
   
        return ans if uf1.size == n and uf2.size == n else -1

