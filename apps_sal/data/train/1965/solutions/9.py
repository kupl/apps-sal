import sys
input = sys.stdin.readline

class Unionfind:
    def __init__(self, n):
        self.par = [-1]*n
        self.rank = [1]*n
    
    def root(self, x):
        r = x
        
        while not self.par[r]<0:
            r = self.par[r]
        
        t = x
        
        while t!=r:
            tmp = t
            t = self.par[t]
            self.par[tmp] = r
        
        return r
    
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        
        if rx==ry:
            return
        
        if self.rank[rx]<=self.rank[ry]:
            self.par[ry] += self.par[rx]
            self.par[rx] = ry
            
            if self.rank[rx]==self.rank[ry]:
                self.rank[ry] += 1
        else:
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
    
    def is_same(self, x, y):
        return self.root(x)==self.root(y)
    
    def count(self, x):
        return -self.par[self.root(x)]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1 = Unionfind(n)
        uf2 = Unionfind(n)
        ans = 0
        
        for t, u, v in edges:
            if t==3:
                if not uf1.is_same(u-1, v-1):
                    uf1.unite(u-1, v-1)
                    uf2.unite(u-1, v-1)
                else:
                    ans += 1
        
        for t, u, v in edges:
            if t==1:
                if not uf1.is_same(u-1, v-1):
                    uf1.unite(u-1, v-1)
                else:
                    ans += 1
            elif t==2:
                if not uf2.is_same(u-1, v-1):
                    uf2.unite(u-1, v-1)
                else:
                    ans += 1
        
        if len(set(uf1.root(i) for i in range(n)))>1:
            return -1
        
        if len(set(uf2.root(i) for i in range(n)))>1:
            return -1
        
        return ans
