class Solution:
    def addEdge(self,source, dest, weight):
        self.graph.append([tuple(source), tuple(dest), weight])
        
    def getParent(self, vertex):
        if vertex == self.parent[vertex]:
            return vertex
        return self.getParent(self.parent[vertex])
        
    def joinTrees(self, u, v):
        xroot = self.getParent(u)
        yroot = self.getParent(v)
        
        if self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        elif self.rank[yroot] < self.rank[xroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            self.rank[yroot]+=1
        
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.graph = []
        
        for i in range(0, len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) 
                self.addEdge(points[i], points[j], dist)
        
        self.V = len(points)
        
        e = 0
        self.parent = {tuple(points[i]): tuple(points[i]) for i in range(0, len(points))}
        self.rank = {tuple(points[i]): 0 for i in range(0, len(points))}
        
        
        self.graph = sorted(self.graph, key = lambda x: x[2])
        
        i = 0
        tot = 0
        
        while e < self.V-1:
            
            u, v, w = self.graph[i]
            i+=1
            uroot = self.getParent(u)
            vroot = self.getParent(v)
            
            if uroot != vroot:
                self.joinTrees(u, v)
                tot+=w
                e+=1
        return tot

