class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        distances = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                distances.append([i, j, self.dist(points[i], points[j])])

        distances.sort(key=lambda x: x[2])

        parent = []
        for i in range(n):
            parent.append(i)

        e = 0
        i = 0
        result = 0
        while e < n - 1:
            u, v, w = distances[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle,
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                e = e + 1
                result += w
                self.union(parent, x, y)

        return result

    def dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if xroot != yroot:
            parent[yroot] = xroot
