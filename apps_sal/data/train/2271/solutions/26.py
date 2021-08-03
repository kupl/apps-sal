class UnionFind:

    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unit(self, x: int, y: int):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        else:
            self.parent[parent_y] = parent_x
            if self.rank[parent_y] == self.rank[parent_x]:
                self.rank[parent_x] += 1

    def same_check(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


N, M = list(map(int, input().split()))

p = list(map(int, input().split()))

xy = UnionFind(N)

for _ in range(M):
    x, y = list(map(int, input().split()))
    xy.unit(x, y)

ans = 0

for i in range(N):
    if xy.same_check(p[i], i + 1):
        ans += 1

print(ans)
