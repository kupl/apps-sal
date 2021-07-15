class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def cost(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        n = len(points)
        dists = []
        for i in range(n):
            for j in range(i + 1, n):
                dists.append((cost(i, j), i, j))
        dists.sort()
        uf = UnionFind(n)
        ans = 0
        for c, i, j in dists:
            if uf.union(i, j):
                ans += c
        return ans
        
class UnionFind:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, i):
        root = i
        while root != self.id[root]:
            root = self.id[root]
        while root != i:
            j = self.id[i]
            self.id[i] = root
            i = j
        return root
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False
        if self.size[root_i] < self.size[root_j]:
            self.id[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        else:
            self.id[root_j] = root_i
            self.size[root_i] += self.size[root_j]
        return True
