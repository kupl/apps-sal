import sys


def input():
    return sys.stdin.readline().strip()


class DisjointSet:
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]


N, M = list(map(int, input().split()))
P = list([int(x) - 1 for x in input().split()])
ds = DisjointSet(N)
for _ in range(M):
    x, y = [int(x) - 1 for x in input().split()]
    ds.union(x, y)
print((sum(ds.same(P[i], i) for i in range(N))))
