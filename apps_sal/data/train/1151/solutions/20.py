from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.n = n
        self.edge = defaultdict(list)

    def addegde(self, u, v):
        self.edge[u].append(v)
        self.edge[v].append(u)

    def dfsUtil(self, i, visited):
        visited[i] = True
        for j in self.edge[i]:
            if visited[j] == False:
                self.dfsUtil(j, visited)

    def dfs(self):
        visited = [False] * self.n
        s = 0
        for i in range(self.n):
            if visited[i] == False:
                s += 1
                self.dfsUtil(i, visited)
        return s


for _ in range(int(input())):
    m, n = map(int, input().split())
    g = Graph(m)
    for i in range(n):
        a, b = map(int, input().split())
        g.addegde(a, b)
    print(g.dfs())
