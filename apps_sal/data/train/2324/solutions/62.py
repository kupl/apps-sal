import sys
sys.setrecursionlimit(10**8)
N = int(input())
G = [[] for i in range(N)]
F = [0 for i in range(N)]
A = []
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    A.append([a, b])


def dfs(s, R):
    F[s] = 1

    if s == N - 1:
        return [s]
    else:
        for n in G[s]:
            if F[n] == 0:
                k = dfs(n, R)
                if len(k) != 0:
                    k.append(s)
                    return k

    return []


root = dfs(0, [])
p = root[::-1][len(root) // 2 + len(root) % 2 - 1]
q = root[::-1][len(root) // 2 + len(root) % 2]


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
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


uf = UnionFind(N)
for i in range(N - 1):
    a, b = map(int, A[i])
    if a == p and b == q:
        continue
    if a == q and b == p:
        continue
    uf.union(a, b)

scoreA = uf.size(0)
scoreB = N - scoreA

if scoreA > scoreB:
    print("Fennec")
else:
    print("Snuke")
