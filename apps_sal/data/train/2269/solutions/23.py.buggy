from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        '木の初期化をする'
        self.p = [-1] * n
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x: int) -> int:
        'x の親を返す'
        if self.p[x] == -1:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def unite(self, x: int, y: int) -> bool:
        'rankの低い親を高い方のの親にする'
        if not self.same(x, y):
            x = self.find(x)
            y = self.find(y)
            if self.rank[x] > self.rank[y]:
                x, y = y, x
            elif self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.p[x] = y
            self.size[y] += self.size[x]
            return True
        else:
            return False

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


n, m = list(map(int, input().split()))
path = [[1] * n for _ in range(n)]
for j in range(n):
    path[j][j] = 0
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    path[a][b] = 0
    path[b][a] = 0

uf = UnionFind(2 * n)

for i in range(n):
    for j in range(n):
        if path[i][j] == 1:
            uf.unite(i, j + n)
            uf.unite(i + n, j)

for i in range(n):
    if uf.same(i, i + n):
        print((-1))
        return

deltas: List[int] = []

view = [1] * n

for i in range(n):
    if view[i] == 0:
        continue
    delta = 0
    for j in range(n):
        if uf.same(i, j):
            view[j] = 0
            delta += 1
        elif uf.same(i, j + n):
            view[j] = 0
            delta -= 1
    delta = abs(delta)
    deltas.append(delta)
dp = [0] * (n + 10)
dp[0] = 1
for delta in deltas:
    dpnxt = [0] * (n + 10)
    for i in range(n + 1):
        if i + delta <= n:
            dpnxt[i + delta] += dp[i]
        dpnxt[abs(i - delta)] += dp[i]
    dp = dpnxt.copy()

for i in range(n + 1):
    if dp[i]:
        print(((n + i) // 2 * ((n + i - 1) // 2) // 2 + (n - i) // 2 * ((n - i - 1) // 2) // 2))
        return
