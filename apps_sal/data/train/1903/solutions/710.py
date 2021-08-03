from functools import cmp_to_key


def cmp(a, b):
    return a[2] - b[2]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []
        points = [tuple(l) for l in points]
        N = len(points)
        if(N == 1):
            return 0

        for i in range(N):
            x, y = points[i]
            for j in range(i + 1, N):
                x1, y1 = points[j]
                edges.append((i, j, abs(x - x1) + abs(y - y1)))
        edges.sort(key=cmp_to_key(cmp))
        parent = {i: i for i in points}
        rank = {i: 0 for i in points}
        val = 0
        ct = 0
        for i, j, v in edges:

            l = self.union(rank, parent, points[i], points[j])
            if(l != 0):
                ct += 1
                val += v
            if(ct == N - 1):
                return val

    def find(self, parent, node):
        if(parent[node] == node):
            return node
        parent[node] = self.find(parent, parent[node])
        return parent[node]

    def union(self, rank, parent, node1, node2):

        x = self.find(parent, node1)
        y = self.find(parent, node2)
        if(x == y):
            return 0
        if(rank[x] > rank[y]):
            parent[y] = x
        elif(rank[x] < rank[y]):
            parent[x] = y
        else:
            rank[x] += 1
            parent[y] = x
        return 1
