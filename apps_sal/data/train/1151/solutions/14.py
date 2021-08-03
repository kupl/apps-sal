from collections import defaultdict


class graph():
    def __init__(self, n):
        self.v = n
        self.adj = defaultdict(list)

    def addedge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def connected(self):
        vis = [False] * self.v
        c = []
        for v in range(self.v):
            if vis[v] == False:
                temp = []
                c.append(self.util(temp, v, vis))
        return c

    def util(self, temp, v, vis):
        vis[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if vis[i] == False:
                temp = self.util(temp, i, vis)
        return temp


t = int(input())
while t > 0:
    t = t - 1
    n, m = list(map(int, input().split()))
    gr = graph(n)
    for i in range(m):
        u, v = list(map(int, input().split()))
        gr.addedge(u, v)
    c = gr.connected()
    print(len(c))
