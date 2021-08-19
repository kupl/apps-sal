import sys


def input():
    return sys.stdin.readline().rstrip()


class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
        else:
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    (N, M) = list(map(int, input().split()))
    P = list([int(x) - 1 for x in input().split()])
    XY = [list([int(x) - 1 for x in input().split()]) for _ in range(M)]
    value_to_index = [0] * N
    for (i, p) in enumerate(P):
        value_to_index[p] = i
    uf = UnionFind(N)
    for (x, y) in XY:
        uf.union(x, y)
    ans = 0
    for i in range(N):
        if uf.find(i) == uf.find(value_to_index[i]):
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
