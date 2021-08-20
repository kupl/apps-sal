import sys


class UnionFind:

    def __init__(self, sz):
        self.__ranks = [1] * sz
        self.__sizes = [1] * sz
        self.__parents = [i for i in range(sz)]

    def find_parent(self, x):
        if x == self.__parents[x]:
            return x
        else:
            self.__parents[x] = self.find_parent(self.__parents[x])
            return self.__parents[x]

    def same(self, x, y):
        return self.find_parent(x) == self.find_parent(y)

    def unite(self, x, y):
        px = self.find_parent(x)
        py = self.find_parent(y)
        if px == py:
            return
        if self.__ranks[px] > self.__ranks[py]:
            self.__parents[py] = px
            self.__sizes[px] += self.__sizes[py]
        else:
            self.__parents[px] = py
            self.__sizes[py] += self.__sizes[px]
            if self.__ranks[px] == self.__ranks[py]:
                self.__ranks[py] += 1

    def size(self, n):
        return self.__sizes[n]


def main():
    n = int(input())
    edge = {}
    for i in range(n - 1):
        (u, v) = list(map(int, sys.stdin.readline().split()))
        if u not in edge:
            edge[u] = []
        if v not in edge:
            edge[v] = []
        edge[u].append(v)
        edge[v].append(u)
    colors = [-1] * (n + 1)
    for (i, c) in enumerate(map(int, sys.stdin.readline().split())):
        colors[i + 1] = c
    uf = UnionFind(n + 1)
    for u in list(edge.keys()):
        for v in edge[u]:
            if colors[u] == colors[v]:
                uf.unite(u, v)
    tree = set()
    for v in range(1, n + 1):
        tree.add(uf.find_parent(v))
    target_v = -1
    ok = False
    for u in range(1, n + 1):
        cnt = set()
        for v in edge[u]:
            cnt.add(uf.find_parent(v))
        if len(cnt) == len(tree) - (1 if uf.size(uf.find_parent(u)) == 1 else 0):
            ok = True
            target_v = u
            break
    if ok:
        print('YES')
        print(target_v)
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
