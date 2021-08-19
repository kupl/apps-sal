class UnionFind:
    def __init__(self, n):
        self.parent = collections.defaultdict(int)
        for i in range(1, n + 1):
            self.parent[i] = i

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, u, v):
        u_parent, v_parent = self.find(u), self.find(v)
        if u_parent == v_parent:
            return False
        self.parent[u_parent] = v_parent
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        connections = list()
        for i in range(n - 1):
            for j in range(i + 1, n):
                # get distance
                connections.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        res = 0
        connections_sorted = sorted(connections, key=lambda arr: arr[2])
        UF = UnionFind(n)
        for connection in connections_sorted:
            a, b, cost = connection
            if UF.find(a) != UF.find(b):
                UF.union(a, b)
                res += cost
        return res
