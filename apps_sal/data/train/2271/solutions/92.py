from collections import Counter
import sys
stdin = sys.stdin


def ip(): return int(sp())
def fp(): return float(sp())


def lp(): return list(map(int, stdin.readline().split()))
def sp(): return stdin.readline().rstrip()
def yp(): return print('Yes')
def np(): return print('No')


class union_find():
    def __init__(self, n):
        self.n = n
        # 親要素のノード番号を格納。par[x]==xのときそのノードは根
        # 親とはその上にノードなし！！　
        self.par = [-1 for i in range(n)]
        self.rank = [0] * (n)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])

            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        # 木の高さを比較し、低い方から高い方へ辺をはる
        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def all_group_member(self):
        return {r: self.members(r) for r in self.roots()}


n, m = lp()
a = lp()
uf = union_find(n)
for _ in range(m):
    x, y = lp()
    uf.union(x - 1, y - 1)

ans = 0
for i in range(n):
    now = a[i] - 1
    if uf.same(i, now):
        ans += 1

print(ans)
