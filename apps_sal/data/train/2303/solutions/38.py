import sys
from collections import deque


class UnionFindVerSize():
    def __init__(self, init):
        """ N個のノードのUnion-Find木を作成する """
        self._parent = [n for n in range(0, len(init))]
        self._size = [1] * len(init)
        self._dict = {key: 0 for key in init}
        for i in range(len(init)):
            v = init[i]
            self._dict[v] = i

    def find_root(self, x, key):
        """ xの木の根(xがどのグループか)を求める """
        if key == 1:
            x = self._dict[x]
        if self._parent[x] == x:
            return x
        self._parent[x] = self.find_root(self._parent[x], 0)
        return self._parent[x]

    def unite(self, x, y):
        """ xとyの属するグループを併合する """
        x = self._dict[x]
        y = self._dict[y]
        gx = self.find_root(x, 0)
        gy = self.find_root(y, 0)
        if gx == gy:
            return

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        x = self._dict[x]
        """ xが属するグループのサイズ（個数）を返す """
        return self._size[self.find_root(x, 0)]

    def is_same_group(self, x, y):
        x = self._dict[x]
        y = self._dict[y]
        """ xとyが同じ集合に属するか否か """
        return self.find_root(x, 0) == self.find_root(y, 0)

    def calc_group_num(self):
        """ グループ数を計算して返す """
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i, 0) == i:
                ans += 1
        return ans


input = sys.stdin.readline

N, M = map(int, input().split())
company = {}
cedge = {}
node = N
edge = {i: [] for i in range(N)}
for i in range(M):
    u, v, c = map(int, input().split())
    edge[u - 1].append((v - 1, 1))
    edge[v - 1].append((u - 1, 1))
    if c - 1 not in company:
        company[c - 1] = []
        cedge[c - 1] = []
    company[c - 1].append(u - 1)
    company[c - 1].append(v - 1)
    cedge[c - 1].append((u - 1, v - 1))

for i in company:
    uf = UnionFindVerSize(company[i])
    for u, v in cedge[i]:
        uf.unite(u, v)
    data = {}
    for v in company[i]:
        p = uf.find_root(v, 1)
        if p not in data:
            data[p] = []
        data[p].append(v)
    for p in data:
        edge[node] = []
        for v in data[p]:
            edge[v].append((node, 0))
            edge[node].append((v, 1))
        node += 1

dist = [10**20] * node
dist[0] = 0
que = deque([(0, 0)])
while que:
    v, d = que.popleft()
    for nv, c in edge[v]:
        if dist[nv] > d + c:
            if c == 1:
                dist[nv] = d + c
                que.append((nv, d + c))
            else:
                dist[nv] = d + c
                que.appendleft((nv, d + c))


ans = dist[N - 1]
print(ans if ans != 10**20 else -1)
