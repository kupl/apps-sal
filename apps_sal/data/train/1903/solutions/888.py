class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dic = {}
        for i in range(len(points)):
            val = []
            for j in range(len(points)):
                if points[j] != points[i]:
                    val = (abs(points[j][0]-points[i][0]) + abs(points[j][1] - points[i][1]))   
                    dic[i,j] = val
        #print(dic)
        g = Graph(len(points))
        
        for k,v in list(dic.items()):
            g.addEdge(k[0],k[1],v)
        
        res = g.KruskalMST()
        print(res)
        return res

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        
    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])
        
    def find(self,parent, i):
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set
        
    def KruskalMST(self):
        MST = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key = lambda e:e[2])
        parent = [-1] * self.v
        while e < self.v -1:
            u,v,w = self.graph[i]
            i += 1
            x = self.find(parent,u)
            y = self.find(parent, v)
            #print(x,y)
            if x!= y:
                e += 1
                MST.append([u,v,w])
                self.union(parent,x,y)
                #print(MST)
        s = 0
        for u,v,w in MST:
            s += w
        return s
        

