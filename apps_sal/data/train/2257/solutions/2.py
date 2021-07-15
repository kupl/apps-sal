import sys
input = sys.stdin.readline


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.cnt = n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.cnt -= 1

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def get_size(self, x):
        return -self.parent[self.root(x)]

    def get_cnt(self):
        return self.cnt


t = int(input())
alph = "abcdefghijklmnopqrstuvwxyz"
to_ind = {char: i for i, char in enumerate(alph)}


for _ in range(t):
    n = int(input())
    a = list(input())
    b = list(input())
    
    flag = False
    for i in range(n):
        if a[i] > b[i]:
            print(-1)
            flag = True
            break
    if flag:
        continue

    uf = UnionFind(26)
    for i in range(n):
        u = to_ind[a[i]]
        v = to_ind[b[i]]
        uf.merge(u, v)
    print(26 - uf.get_cnt())
