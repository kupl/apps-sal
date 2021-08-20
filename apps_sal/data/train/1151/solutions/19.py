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
        return len(cc)


def __starting_point():
    t = int(input())
    for _ in range(t):
        (n, m) = list(map(int, input().strip().split()))
        g = Graph(n)
        for _ in range(m):
            (a, b) = list(map(int, input().strip().split()))
            g.addEdge(a, b)
        cc = g.connectedComponents()
        print(cc)


__starting_point()
