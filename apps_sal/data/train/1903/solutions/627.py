class UnionFind:
    def __init__(self, n):
        self.sets = {i : i for i in range(n)}
        self.n_sets = n
    def find(self, s):
        if self.sets[s] != s:
            self.sets[s] = self.find(self.sets[s])
        return self.sets[s]
    def union(self, s1, s2):
        a, b = self.find(s1), self.find(s2)
        if a == b:
            return False
        self.sets[a] = b
        self.n_sets -= 1
        return True
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        N = len(points)
        for i in range(N):
            for j in range(i + 1, N):
                p1, p2 = points[i], points[j]
                edges.append((abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), i, j))
        edges.sort()
        uf = UnionFind(N)
        res = 0
        for w, u, v in edges:
            if uf.union(u, v):
                res += w
            # if uf.n_sets == 1:
            #     break
        return res
