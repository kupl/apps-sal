from collections import deque
import sys


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        self.group = {r: [] for r in self.roots()}
        for i in range(self.n):
            self.group[self.find(i)].append(i)
        return self.group

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


input = sys.stdin.readline
(n, m) = map(int, input().split())
uf = UnionFind(n)
e = [[] for _ in range(n)]
for i in range(m):
    (u, v, c) = map(int, input().split())
    u -= 1
    v -= 1
    if uf.same(u, v):
        continue
    e[u].append((v, c))
    e[v].append((u, c))
que = deque()
que.append(0)
ans = [-1] * n
ans[0] = 1
while que:
    now = que.popleft()
    for (i, j) in e[now]:
        if ans[i] != -1:
            continue
        if ans[now] == j:
            ans[i] = (j + 1) % n
            if ans[i] == 0:
                ans[i] = n
        else:
            ans[i] = j
        que.append(i)
print(*ans, sep='\n')
