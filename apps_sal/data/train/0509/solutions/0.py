import sys
sys.setrecursionlimit(10**6)

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

n, m = map(int, input().split())

ans = [-1]*n

uf = UnionFind(n)
g = [[] for i in range(n)]

for i in range(m):
    u, v, c = map(int, input().split())
    if not uf.same(u-1, v-1):
        uf.union(u-1, v-1)
        g[u-1].append((v-1, c))
        g[v-1].append((u-1, c))

def dfs(i):
    for to, c in g[i]:
        if ans[to]==-1:
            if ans[i] == c:
                if c == 1:
                    ans[to] = c+1
                else:
                    ans[to] = c-1
            else:
                ans[to] = c
            dfs(to)

ans = [-1]*n
ans[0] = 1
dfs(0)

if -1 in ans:
    print('No')
    return

ans = [a for a in ans]

print(*ans, sep='\n')

