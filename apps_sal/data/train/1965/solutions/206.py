class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.sz[yr] = self.sz[xr]
        return True

    def size(self, x):
        return self.sz[self.find(x)]
    

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        edges.sort(reverse=True)
        
        bob = DSU(n)
        alice = DSU(n)
        
        res = 0
        
        for t, a, b in edges:
            a -= 1
            b -= 1
            if t == 3 and (bob.find(a) != bob.find(b) or alice.find(a) != alice.find(b)):
                bob.union(a, b)
                alice.union(a, b)
            elif t == 2 and bob.find(a) != bob.find(b):
                bob.union(a, b)
            elif t == 1 and alice.find(a) != alice.find(b):
                alice.union(a, b)
            else:
                res += 1
        
        is_one = lambda dsu: len({dsu.find(i) for i in range(n)}) == 1
        
        return res if is_one(alice) and is_one(bob) else -1

