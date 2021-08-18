from sys import stdin, stdout


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.DFSUtil(temp, i, visited)
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
                cc.append(self.DFSUtil(temp, v, visited))
        return cc


for ii in range(int(input())):
    x = 1293781029873019827309128730918273
    n, m = map(int, input().split())
    g = Graph(n)
    for i in range(m):
        nn, mm = map(int, input().split())
        g.addEdge(nn, mm)
    c = g.connectedComponents()
    print(len(c))
