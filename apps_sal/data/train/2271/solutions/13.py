from collections import defaultdict


class UnionFind():
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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def slove():
    N, M = map(int, input().split())
    u = UnionFind(N)
    P = list(map(int, input().split()))
    for _ in range(M):
        x, y = map(int, input().split())
        u.union(x - 1, y - 1)
    ans = 0
    for i, p in enumerate(P):
        if p - 1 in u.members(i):
            ans += 1
    print(ans)


def slove2():
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    l = list(range(N + 1))

    def find(p):
        if l[p] == p:
            return p
        else:
            l[p] = find(l[p])
            return l[p]
    for _ in range(M):
        x, y = map(int, input().split())
        x = find(x)
        y = find(y)
        if x > y:
            x, y = y, x
        l[y] = find(x)
    ans = 0
    for i, p in enumerate(P):
        if find(i + 1) == find(p):
            ans += 1
    print(ans)


def __starting_point():
    slove2()


__starting_point()
