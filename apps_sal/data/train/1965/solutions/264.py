class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.sz = [1]*n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            if self.sz[xr] < self.sz[yr]:
                xr, yr = yr, xr
            self.parent[yr] = xr
            self.sz[xr] += self.sz[yr]
            return True
        return False
    
    def size(self, x):
        return self.sz[self.find(x)]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        graphA, graphB, graphC = [], [], []
        for t, u, v in edges:
            if t == 1:
                graphA.append([u-1, v-1])
            elif t == 2:
                graphB.append([u-1, v-1])
            else:
                graphC.append([u-1, v-1])
        
        alice = DSU(n)
        bob = DSU(n)
        result = 0
        
        for u, v in graphC:
            alice.union(u, v)
            if not bob.union(u, v):
                result += 1
        
        for u, v in graphA:
            if not alice.union(u, v):
                result += 1
        
        for u, v in graphB:
            if not bob.union(u, v):
                result += 1
        
        if alice.size(0) < n or bob.size(0) < n:
            return -1
        
        return result
