class UnionFind():
    def __init__(self, n):
        self.label = list(range(n))
        self.sz = [1] * n
        
    def find(self, p):
        while p != self.label[p]:
            self.label[p] = self.label[self.label[p]]
            p = self.label[p]
        return p
    
    def union(self, p, q):
        proot, qroot = self.find(p), self.find(q)
        if self.sz[proot] >= self.sz[qroot]:
            self.label[qroot] = proot
            self.sz[proot] += self.sz[qroot]
        else:
            self.label[proot] = qroot
            self.sz[qroot] += self.sz[proot]
    
    def size(self, p):
        return self.sz[self.find(p)]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        \"\"\"
        MST, union find?
        
        construct uf based on type 3
        try type 1 and type2 separate
        for a type:
          pick from all edges to achieve reachability
        \"\"\"
        
        def mst(uf, edges):
            result = 0
            for a, b in edges:
                if uf.find(a - 1) == uf.find(b - 1):
                    continue
                uf.union(a - 1, b - 1)
                result += 1
            if uf.size(0) != n:
                return -1
            return result
        
        def commonUf(edges):
            uf = UnionFind(n)
            edgesNeeded = 0
            for a, b in edges:
                if uf.find(a - 1) == uf.find(b - 1):
                    continue
                uf.union(a - 1, b - 1)
                edgesNeeded += 1
            return uf, edgesNeeded
        
        commonEdges = [(edge[1], edge[2]) for edge in edges if edge[0] == 3]
        
        uf1, commonEdgesNeeded = commonUf(commonEdges)
        mst1 = mst(uf1, [(edge[1], edge[2]) for edge in edges if edge[0] == 1])
        uf2, _ = commonUf(commonEdges)
        mst2 = mst(uf2, [(edge[1], edge[2]) for edge in edges if edge[0] == 2])
        
        if mst1 == -1 or mst2 == -1:
            return -1
        return len(edges) - commonEdgesNeeded - mst1 - mst2
        
