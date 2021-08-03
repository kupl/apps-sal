class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x


n, m = map(int, input().split())

g = [[] for _ in range(n)]
uf = UnionFind(n)
for _ in range(m):
    u, v, c = map(lambda x: int(x) - 1, input().split())
    if uf.find(u) != uf.find(v):
        g[u].append([v, c])
        g[v].append([u, c])
        uf.union(u, v)
# print(g)


node_val = [None] * n
node_val[0] = 0
que = [0]
seen = set()
# BFS
while que != []:
    temp = []
    for node in que:
        if node in seen:
            continue
        for next_node, c in g[node]:
            if next_node in seen:
                continue
            if node_val[node] == c:
                node_val[next_node] = (c + 1) % n
            else:
                node_val[next_node] = c

            # update
            temp.append(next_node)

        seen.add(node)

    que = temp

for val in node_val:
    print(val + 1)
