import sys
sys.setrecursionlimit(10 ** 6)
readline = sys.stdin.readline


class UnionFind:

    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        stack = []
        tbl = self.table
        while tbl[x] >= 0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2


def main():
    (N, M) = map(int, readline().split())
    all_edges = [tuple(map(int, readline().split())) for _ in range(M)]
    G = [[] for _ in range(N + 1)]
    edges = []
    edge_to_label = {}
    U = UnionFind(N + 1)
    while all_edges:
        (u, v, c) = all_edges.pop()
        if U.find(u, v):
            continue
        U.union(u, v)
        G[u].append(v)
        G[v].append(u)
        edges.append((u, v))
        edge_to_label[u, v] = c
        edge_to_label[v, u] = c
    label = [0] * (N + 1)
    label[1] = 1
    stack = [1]
    while stack:
        x = stack.pop()
        for y in G[x]:
            if label[y] > 0:
                continue
            l = edge_to_label[x, y]
            if label[x] == l:
                label[y] = (l + 1) % N + 1
                stack.append(y)
            else:
                label[y] = l
                stack.append(y)
    print(*label[1:], sep='\n')


def __starting_point():
    main()


__starting_point()
