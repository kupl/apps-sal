class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]] # path halving
            i = self.parents[i]
        return i
    
    def union(self, a, b):
        aPar = self.find(a)
        bPar = self.find(b)
        
        if aPar == bPar:
            return False
        
        # union by size
        if self.size[aPar] > self.size[bPar]:
            self.parents[bPar] = aPar
            self.size[aPar] += self.size[bPar]
        else:
            self.parents[aPar] = bPar
            self.size[bPar] += self.size[aPar]
        
        return True
    
    def getSize(self, a):
        return self.size[self.find(a)]

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def getDistance(a,b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        N = len(points)
        uf = UnionFind(N)
        edges = []
        
        for i in range(N):
            for j in range(i+1, N):
                edges.append((getDistance(points[i], points[j]), i, j))
                
        edges.sort(key=lambda x:x[0])
        
        cost = 0
        seen = 0
        for w,a,b in edges:
            if uf.union(a,b):
                cost += w
                i += 1
                if seen == N:
                    break
                    
        return cost

