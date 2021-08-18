import heapq


def dijkstra(v, s, path):
    inf = float('inf')

    d = [inf for i in range(v)]
    d[s] = 0

    q = [[0, s]]
    heapq.heapify(q)

    while q:
        p = heapq.heappop(q)

        if d[p[1]] < p[0]:
            continue

        for i in range(len(path[p[1]])):
            if d[path[p[1]][i][1]] > d[p[1]] + path[p[1]][i][0]:
                d[path[p[1]][i][1]] = d[p[1]] + path[p[1]][i][0]
                heapq.heappush(q, [d[path[p[1]][i][1]], path[p[1]][i][1]])
    return d


def path_recovery(e, d, path):
    route = [e]
    a = d[e]
    while a != 0:
        for i in range(len(path[e])):
            if d[path[e][i][1]] + path[e][i][0] == a:
                route.append(path[e][i][1])
                a -= path[e][i][0]
                e = path[e][i][1]
                break
    route.reverse()
    return route


class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[x] += self.par[y]
            self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]


n = int(input())

l = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    l[a - 1].append([1, b - 1])
    l[b - 1].append([1, a - 1])

d = dijkstra(n, 0, l)

p = path_recovery(n - 1, d, l)

x = p[(len(p) - 1) // 2]
y = p[(len(p) - 1) // 2 + 1]

for i in range(len(l[x])):
    if l[x][i][1] == y:
        l[x].pop(i)
        break
for i in range(len(l[y])):
    if l[y][i][1] == x:
        l[y].pop(i)
        break

u = UnionFind(n)

for i in range(len(l)):
    for j in range(len(l[i])):
        u.unite(i, l[i][j][1])


if u.size(0) > u.size(n - 1):
    print('Fennec')
else:
    print('Snuke')
