class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a_uf = UF(n+1)
        b_uf = UF(n+1)
        unwanted = 0

        for t, u, v in edges:    
            if t == 3:            
                # Alice and Bob
                if a_uf.find(u) == a_uf.find(v) and b_uf.find(u) == b_uf.find(v):
                    # both guys dont need
                    unwanted += 1
                else:
                    a_uf.union(u, v)
                    b_uf.union(u, v)
        
        for t, u, v in edges:
            #print((t, u, v))
            if t == 1:
                # Alice
                if a_uf.find(u) == a_uf.find(v):
                    # dont need this
                    unwanted += 1
                else:
                    a_uf.union(u, v)
        for t, u, v in edges:    
            if t == 2:
                # Bob
                if b_uf.find(u) == b_uf.find(v):
                    # dont need this
                    unwanted += 1
                else:
                    b_uf.union(u, v)
                
        if a_uf.size[a_uf.find(1)] < n or b_uf.size[b_uf.find(1)] < n:
            return -1
                
        return unwanted
    
class UF:
    def __init__(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, u):
        while u != self.uf[u]:
            self.uf[u] = self.uf[self.uf[u]]
            u = self.uf[u]
        return u
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.size[rootU] > self.size[rootV]:
                self.size[rootU] += self.size[rootV]
                self.uf[rootV] = rootU
            else:
                self.size[rootV] += self.size[rootU]
                self.uf[rootU] = rootV
        
        

