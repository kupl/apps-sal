# cook your dish here
from collections import defaultdict

class sol():
    def __init__(self,n,edges):
        self.n = n
        self.edges = edges
        self.graph = self.create_graph()
        self.precompute()
        
    def create_graph(self):
        graph = defaultdict(list)
        for e in self.edges:
            u = e[0]
            v = e[1]
            w = e[2]
            graph[u].append([v,w])
            graph[v].append([u,w])
        return graph
        
    def precompute(self):
        self.maxiedges = [0]*6
        self.B = [[0 for i in range(101)] for i in range(101)]
        def func(u,v,l):
            if l==2:
                self.B[u][self.maxiedges[l]] += 1
            else:
                for j in self.graph[v]:
                    self.maxiedges[l+1] = max(self.maxiedges[l],j[1])
                    func(u,j[0],l+1)
        for i in range(1,self.n+1):
            func(i,i,0)
            
    def paths(self,X):
        freq = 0
        for u in range(1,self.n+1):
            for x in range(X+1):
                freq += 2*self.B[u][X]*self.B[u][x]
            freq -= self.B[u][X]*self.B[u][X]
        return freq
        
n, m = map(int, input().split())
edges = []
while m:
    uvw = list(map(int, input().split()))
    edges.append(uvw)
    m -= 1
q = int(input())
Graph = sol(n,edges)
while q:
    query = int(input())
    print(Graph.paths(query))
    q -= 1

