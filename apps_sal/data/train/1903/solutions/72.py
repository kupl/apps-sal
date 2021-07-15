class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        p_x, p_y = self.find(x), self.find(y)
        
        if p_x == p_y:
            return 
        
        if self.rank[p_x] < self.rank[p_y]:
            self.parent[p_x] = p_y
            self.rank[p_y] += self.rank[p_x]
        else:
            self.parent[p_y] = p_x
            self.rank[p_x] += self.rank[p_y]
        
        
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build graph by using edge list (x, y, weight)
        n = len(points)
        
        edge_list = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    edge_list.append([i, j, self.dist(points[i], points[j])])
        
        # find the final result: each time select the edge with minimun weight, and vertices come from different component, merge the component, add the cost
        uf = UnionFind(n)
        cost = 0
        edge_list.sort(key = lambda x : x[2])
        
        for u, v, w in edge_list:
            p_u, p_v = uf.find(u), uf.find(v)
            
            if p_u == p_v:
                continue
            
            uf.union(u, v)
            cost += w
        
        return cost
    
    def dist(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                

