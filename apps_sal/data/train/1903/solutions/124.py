from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        return kruskal(points)


class UnionFind:
    
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.rank = [0]*N
    
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def union(self, x, y):
        
        xpar = self.find(x)
        ypar = self.find(y)
        
        if self.rank[xpar] > self.rank[ypar]:
            self.par[ypar] = xpar
        elif  self.rank[xpar] < self.rank[ypar]:
            self.par[xpar] = ypar
        elif self.rank[xpar] == self.rank[ypar]:
            self.par[xpar] = ypar
            self.rank[xpar] += 1
            
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
            

def kruskal(points):
    
    n     = len(points)
    V     = UnionFind(n)
    #mst   = set()
    edges = set()
    
    for i, (x1, y1) in enumerate(points):
        for j, (x2, y2) in enumerate(points):
            edges.add((i,j,abs(x2-x1)+abs(y2-y1)))

    edges = sorted(edges, key=lambda e: e[2])
    
    cost = 0
    for e in edges:
        
        i, j, w = e
        if V.connected(i,j):
            continue
        
        V.union(i,j)
        #mst.add(i)
        #mst.add(j)
        cost += w
    return cost    

