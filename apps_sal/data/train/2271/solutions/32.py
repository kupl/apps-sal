class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.members = [{i} for i in range(n)]
        self.roots = {i for i in range(n)}

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def union(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.par[rx] = ry
                self.members[ry] |= self.members[rx]
                self.roots.discard(rx)
            else:
                self.par[ry] = rx
                self.members[rx] |= self.members[ry]
                self.roots.discard(ry)
                if self.rank[rx] == self.rank[ry]:
                    self.rank[rx] += 1

    def same(self, x, y):
        return self.root(x) == self.root(y)


(N, M) = list(map(int, input().split()))
P = list([int(x) - 1 for x in input().split()])
X = UnionFind(N)
Y = UnionFind(N)
for _ in range(M):
    (x, y) = list(map(int, input().split()))
    x -= 1
    y -= 1
    X.union(x, y)
    Y.union(P[x], P[y])
ans = 0
roots = X.roots
for r in roots:
    A = X.members[r]
    B = Y.members[P[r]]
    ans += len(A & B)
print(ans)
