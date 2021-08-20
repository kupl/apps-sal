import sys


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


class UnionFind:
    """ 0-indexed Union Find Tree (a.k.a Disjoint Union Tree)
    """

    def __init__(self, n: int):
        self.nodes = n
        self.parents = [-1] * n
        self.rank = [0] * n

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
        if self.rank[x] < self.rank[y]:
            self.parents[y] += self.parents[x]
            self.parents[x] = y
        else:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def get_size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_groups(self, index_base=0) -> list:
        d = {}
        for i in range(index_base, self.nodes):
            p = self.find(i)
            if p not in list(d.keys()):
                d[p] = set()
            d[p].add(i)
        return list(d.values())


def main():
    (n, m) = input_int_list()
    A = [None] + input_int_list()
    djs = UnionFind(n + 1)
    for _ in range(m):
        (x, y) = input_int_list()
        djs.unite(x, y)
    groups = djs.get_groups()
    ans = 0
    for group in groups:
        v = set()
        for i in group:
            v.add(A[i])
        ans += len(group & v)
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
