class UnionFind:

    def __init__(self, n):
        self.N = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def root(self, x):
        visited_nodes = []
        while True:
            p = self.parent[x]
            if p == x:
                for node in visited_nodes:
                    self.parent[node] = x
                return x
            else:
                visited_nodes.append(x)
                x = p

    def unite(self, x, y):
        if not self.root(x) == self.root(y):
            if self.rank[x] > self.rank[y]:
                self.parent[self.root(y)] = self.root(x)
            else:
                self.parent[self.root(x)] = self.root(y)
                if self.rank[x] == self.rank[y]:
                    self.rank[self.root(y)] += 1

    def ifSame(self, x, y):
        return self.root(x) == self.root(y)

    def printDebugInfo(self):
        print([self.root(i) for i in range(self.N)])


(N, M) = list(map(int, input().split()))
P = [int(x) for x in input().split()]
tree = UnionFind(N)
for _ in range(M):
    (X, Y) = list(map(int, input().split()))
    tree.unite(X - 1, Y - 1)
count = 0
for i in range(N):
    if tree.ifSame(P[i] - 1, i):
        count += 1
print(count)
