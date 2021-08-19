# cook your dish here
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def dfs(self, temp, v, visited):
        visited[v] = True
        temp.append(v)

        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.dfs(temp, i, visited)
        return temp

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.dfs(temp, v, visited))
        return cc


for _ in range(int(input())):
    N, M = map(int, input().split())
    g = Graph(N)
    for i in range(M):
        a, b = map(int, input().split())
        g.addEdge(a, b)
    print(len(g.connectedComponents()))
