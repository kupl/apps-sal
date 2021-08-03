class DSU(object):
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        rootA, rootB = self.find(x), self.find(y)
        if rootA != rootB:
            self.parents[rootA] = rootB


def solve():
    n, m = map(int, input().split())
    dsu = DSU(n)
    for i in range(m):
        x, y = map(int, input().split())
        dsu.union(x, y)
    cnt = 0
    for i, x in enumerate(dsu.parents):
        cnt += (i == x)
    print(cnt)


t = int(input())
while t:
    solve()
    t -= 1
