class dsu:
    def __init__(self, n):
        self.parent = [-1 for i in range(n)]
        self.size = [0 for i in range(n)]

    def make_set(self, node):
        self.parent[node] = node

    def find(self, a):
        if self.parent[a] == a:
            return self.parent[a]
        else:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.parent[b] = self.parent[a]


class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        n = len(p)
        if n <= 1:
            return 0
        tree = dsu(n)
        edges = []
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                edges.append([abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1]), i, j])
        edges.sort()
        done = 0
        ans = 0
        for i in range(n):
            tree.make_set(i)
        for i in edges:

            if tree.find(i[1]) != tree.find(i[2]):
                done = done + 1
                ans = ans + i[0]
                tree.union(i[1], i[2])
        return ans
