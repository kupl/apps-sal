import sys
input = sys.stdin.readline


class Unionfind:

    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [1] * n

    def root(self, x):
        p = x
        while not self.par[p] < 0:
            p = self.par[p]
        while x != p:
            tmp = x
            x = self.par[x]
            self.par[tmp] = p
        return p

    def unite(self, x, y):
        (rx, ry) = (self.root(x), self.root(y))
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            (rx, ry) = (ry, rx)
        self.par[rx] += self.par[ry]
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def count(self, x):
        return -self.par[self.root(x)]


n = int(input())
a = list(map(int, input().split()))
p = list(map(int, input().split()))
uf = Unionfind(n)
V = [0] * n
flag = [False] * n
ans = [0]
for pi in p[::-1]:
    pi -= 1
    V[pi] = a[pi]
    flag[pi] = True
    if pi - 1 >= 0 and flag[pi - 1]:
        v = V[uf.root(pi - 1)] + V[uf.root(pi)]
        uf.unite(pi - 1, pi)
        V[uf.root(pi)] = v
    if pi + 1 < n and flag[pi + 1]:
        v = V[uf.root(pi + 1)] + V[uf.root(pi)]
        uf.unite(pi, pi + 1)
        V[uf.root(pi)] = v
    ans.append(max(ans[-1], V[uf.root(pi)]))
for ans_i in ans[:-1][::-1]:
    print(ans_i)
