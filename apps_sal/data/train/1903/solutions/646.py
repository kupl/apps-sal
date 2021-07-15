class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        uf = UF(len(points))
        n = len(points)
        for i, ps in enumerate(points):
            j = i+1
            while j < n:
                pt = points[j]
                dist = abs(ps[0]-pt[0]) + abs(ps[1]-pt[1])
                uf.addEdge(i, j, dist)
                j += 1
                
        return uf.KruskalMST()
                    
                    
class UF:
    def __init__(self, n):
        self.n = n
        self.g = []
        
    def addEdge(self, s, t, cost):
        self.g.append((s, t, cost))
        
    def find(self, x, parent):
        if parent[x] == x:
            return x
        
        return self.find(parent[x], parent)
    
    def union(self, x, y, parent, rank):
        xroot, yroot = self.find(x, parent), self.find(y, parent)
        if xroot != yroot:
            if rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
                return xroot
            elif rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
                return yroot
            
            else:
                parent[yroot] = xroot
                rank[xroot] += 1
                return xroot
                
        else:
            return xroot
        
    def KruskalMST(self):
        parent = [_ for _ in range(self.n)]
        rank = [0]*self.n
        # print(self.find(1, parent))
        # print(self.union(1,2, parent, rank))
        # print(self.union(1,3, parent, rank))
        # print(parent, rank)
        # print(self.g)
        self.g.sort(key = lambda edge: edge[2])
        # print(self.g)
        totalans = 0
        for edge in self.g:
            x = edge[0]
            y = edge[1]
            xroot = self.find(x, parent)
            yroot = self.find(y, parent)
            
            if xroot != yroot:
                self.union(x, y, parent, rank)
                totalans += edge[2]
                
                
        return(totalans)
                    

