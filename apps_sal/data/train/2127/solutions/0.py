class DisjointSet(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num = n

    def union(self, x, y):
        self._link(self.find_set(x), self.find_set(y))

    def _link(self, x, y):
        if x == y:
            return
        self.num -= 1
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def find_set(self, x):
        xp = self.parent[x]
        if xp != x:
            self.parent[x] = self.find_set(xp)
        return self.parent[x]


def solve():
    n, m = list(map(int, input().split()))
    ds = DisjointSet(n * 2)
    for i in range(m):
        a, b, c = list(map(int, input().split()))
        a -= 1
        b -= 1
        aA = a * 2
        aB = aA + 1
        bA = b * 2
        bB = bA + 1
        if c == 0:
            if ds.find_set(aA) == ds.find_set(bA):
                return 0
            ds.union(aA, bB)
            ds.union(aB, bA)
        else:
            if ds.find_set(aA) == ds.find_set(bB):
                return 0
            ds.union(aA, bA)
            ds.union(aB, bB)
    return pow(2, (ds.num // 2) - 1, 10**9 + 7)


print(solve())
