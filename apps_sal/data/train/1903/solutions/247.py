class Node:
    def __init__(self,data,rank,node):        
        self.data = data
        self.rank = rank
        self.node = node            
        self.parent = self

class UnionFind(object):
    def __init__(self,n):
        self._parent = [0]*n
        self._size = [1]*n
        self.count = n
        for i in range(n):
            self._parent[i] = i
            
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return False
        self.count -= 1
        if self._size[rootp] > self._size[rootq]:
            self._size[rootp] += self._size[rootq]
            self._parent[rootq] = self._parent[q] = rootp
        else:
            self._size[rootq] += self._size[rootp]
            self._parent[rootp] = self._parent[p] = rootq
        return True
    
    def find(self, n):
        while self._parent[n] != n:
            self._parent[n] = self._parent[self._parent[n]]
            n = self._parent[n]
        return n
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
            

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def findManhattanDistance(p1,p2):            
            return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])
        
        edges = []        
        N = len(points)  
        for i,p1 in enumerate(points):
            for j in range(i+1,N):                
                edges.append([i,j,findManhattanDistance(p1,points[j])])                
        
        edges = sorted(edges,key=lambda x:x[2])        
              
        hashMap = {}        
        for i in range(N):            
            node = Node(i,0,None)                     
            hashMap[node.data] = node       
            
        uf = UnionFind(N)
        edge_count = 0
        costs = 0        
        for u,v,w in edges:            
            if(uf.union(u,v)):        
                costs += w
                edge_count +=1
            if(edge_count == N - 1):
                break
        return costs
