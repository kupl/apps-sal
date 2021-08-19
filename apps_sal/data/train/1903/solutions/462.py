class Solution:

    def getWeight(self, x, y):
        (xi, xj) = (x[0], x[1])
        (yi, yj) = (y[0], y[1])
        return abs(xi - yi) + abs(xj - yj)

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        E = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                u = points[i]
                v = points[j]
                E.append([i, j, self.getWeight(u, v)])
        E = sorted(E, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(len(points)):
            parent.append(node)
            rank.append(0)
        e = 0
        i = 0
        result = 0
        while e < len(points) - 1:
            (u, v, w) = E[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result += w
                self.union(parent, rank, x, y)
        return result
