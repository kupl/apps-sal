import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


class UnionFindPathCompression:

    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        elif self.rank[px] < self.rank[py]:
            self.parents[px] = py
            self.size[py] += self.size[px]
        else:
            self.parents[py] = px
            self.size[px] += self.size[py]
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1


(n, m) = map(int, input().split())
P = list(map(int, input().split()))
ufpc = UnionFindPathCompression(n)
for i in range(m):
    (x, y) = map(int, input().split())
    (x, y) = (x - 1, y - 1)
    ufpc.union(x, y)
ans = 0
for (i, p) in enumerate(P):
    if ufpc.find(i) == ufpc.find(p - 1):
        ans += 1
print(ans)
