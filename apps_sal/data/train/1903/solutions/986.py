class Union:
    
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0
        
    def add(self, idx):
        if idx not in self.parent:
            self.parent[idx] = idx
            self.rank[idx] = 1
            self.count += 1
    
    def find(self, idx):
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]
    
    def unite(self, p, q):
        i, j = self.find(p), self.find(q)
        if i == j:
            return True
        if self.rank[i] > self.rank[j]:
            i, j = j, i
        self.parent[i] = j
        self.rank[j] += self.rank[i]
        self.count -= 1
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #p_to_cost = {}
        costs = []
        point = Union()
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                #p_to_cost[(i, j)] = val
                costs.append([i, j, cost])
        costs.sort(key=lambda x: x[2])
        res = 0
        for i, j, c in costs:
            point.add(i)
            point.add(j)
            if not point.unite(i, j):
                res += c
        return res
