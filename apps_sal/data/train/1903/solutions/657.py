class Solution:
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def KruskalMST(self, V, graph): 
        wts = 0
        i = 0 
        e=0
        graph = sorted(graph,key=lambda item: item[2]) 
        parent, rank = [], [] 

        for node in range(V): 
            parent.append(node) 
            rank.append(0) 

        while e < V -1 : 
            u,v,w = graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            if x != y: 
                e+=1
                wts += w
                self.union(parent, rank, x, y)\t\t\t 
        return wts
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        v = len(points)
        edges = []
        for e1, i in enumerate(points):
            for e2, j in enumerate(points):
                if e1!=e2:
                    edges.append([e1, e2, (abs(i[0]-j[0])+abs(i[1]-j[1]))])
        return (self.KruskalMST(v, edges))




