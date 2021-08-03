class UnionFind:
    def __init__(self, num):
        self.parent = [i for i in range(num + 1)]

    def find(self, node):
        if self.parent[node] == node:
            return node

        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)

        if node1 == node2:
            return

        if self.parent[node1] > self.parent[node2]:
            node1, node2 = node2, node1

        self.parent[node2] = node1
        return

    def same(self, node1, node2):
        return self.find(node1) == self.find(node2)


n, m = list(map(int, input().split()))
p = list(map(int, input().split()))

uf = UnionFind(n)
for _ in range(m):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    uf.union(p[x], p[y])

ans = 0
for i in range(n):
    if p[i] == i + 1 or uf.same(p[i], i + 1):
        ans += 1

print(ans)
