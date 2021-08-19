n, a, b = list(map(int, input().split()))
xlist = list(map(int, input().split()))


class UnionFind(list):

    def __init__(self, length):
        super().__init__((-1 for _ in range(length)))

    def root(self, i):
        if self[i] < 0:
            return i
        else:
            self[i] = self.root(self[i])
            return self[i]

    def size(self, i):
        root_i = self.root(i)
        return -1 * self[root_i]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx == ry:
            return
        # unite by size
        if self.size(x) < self.size(y):
            rx, ry = ry, rx
        self[rx] += self[ry]
        self[ry] = rx


un = UnionFind(n)
for i in range(n - 1):
    if (xlist[i + 1] - xlist[i]) * a <= b:
        un.unite(i, i + 1)

ans = 0
for i in range(n - 1):
    if un.same(i, i + 1):
        ans += (xlist[i + 1] - xlist[i]) * a
    else:
        ans += b
print(ans)
