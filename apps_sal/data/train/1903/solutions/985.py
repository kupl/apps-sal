class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []

        for i in range(N):
            a = tuple(points[i])

            for j in range(N):
                if i == j:
                    continue
                b = tuple(points[j])
                cost = abs(a[0] - b[0]) + abs(a[1] - b[1])
                edges.append((cost, i, j))

        edges.sort()

        dsu = DSU(N)
        mst = 0

        for cost, a, b in edges:
            if dsu.union(a, b):
                mst += cost

        return mst


class DSU():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota == rootb:
            return False
        if self.size[roota] < self.size[rootb]:
            self.size[rootb] += self.size[roota]
            self.parent[roota] = rootb
        else:
            self.size[roota] += self.size[rootb]
            self.parent[rootb] = roota
        return True

    def find(self, a):
        root = self.parent[a]
        while root != self.parent[root]:
            root = self.parent[root]
        curr = a

        while curr != root:
            after = self.parent[curr]
            self.parent[curr] = root
            curr = after

        return root
