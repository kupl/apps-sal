from collections import deque


class Unionfind:

    def __init__(self, n):
        self.uf = [-1] * n

    def find(self, x):
        if self.uf[x] < 0:
            return x
        else:
            self.uf[x] = self.find(self.uf[x])
            return self.uf[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.uf[x] > self.uf[y]:
            (x, y) = (y, x)
        self.uf[x] += self.uf[y]
        self.uf[y] = x
        return True

    def size(self, x):
        x = self.find(x)
        return -self.uf[x]


(n, m) = map(int, input().split())
e = [[] for i in range(n + 1)]
uf = Unionfind(n + 1)
for i in range(m):
    (u, v, c) = map(int, input().split())
    if uf.same(u, v):
        continue
    e[u].append((v, c))
    e[v].append((u, c))
ans = [-1] * (n + 1)
ans[1] = 1
q = deque([[1, 0]])
while q:
    (now, par) = q.popleft()
    for (nex, col) in e[now]:
        if ans[nex] > 0:
            continue
        if ans[now] == col:
            ans[nex] = col % n + 1
        else:
            ans[nex] = col
        q.append([nex, now])
for i in ans[1:]:
    print(i)
