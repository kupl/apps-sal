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


for _ in range(int(input())):

    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        x, y = map(int, input().split())
        g.addEdge(x, y)

    cc = g.connectedComponents()
    print(len(cc))
