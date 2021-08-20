class UnionFindTree:

    def __init__(self, n):
        self.nodes = [-1] * n

    def find(self, i):
        if self.nodes[i] < 0:
            return i
        else:
            self.nodes[i] = self.find(self.nodes[i])
            return self.nodes[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return
        if self.nodes[i] > self.nodes[j]:
            (i, j) = (j, i)
        self.nodes[i] += self.nodes[j]
        self.nodes[j] = i

    def size(self, i):
        i = self.find(i)
        return -self.nodes[i]


(n, m) = list(map(int, input().split()))
p = list([int(x) - 1 for x in input().split()])
uft = UnionFindTree(n)
for _ in range(m):
    (x, y) = [int(x) - 1 for x in input().split()]
    uft.union(x, y)
ans = 0
for i in range(n):
    if uft.find(p[i]) == uft.find(i):
        ans += 1
print(ans)
