class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return False

        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        elif self.rank[yRoot] > self.rank[xRoot]:
            self.parent[xRoot] = yRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        pq = []

        for i in range(N):
            for j in range(i):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                pq.append((dist, i, j))

        heapify(pq)
        dsu = DSU(N)
        edges = 0
        cost = 0

        while edges < N - 1:
            dist, i, j = heappop(pq)

            if dsu.union(i, j):
                cost += dist
                edges += 1

        return cost
