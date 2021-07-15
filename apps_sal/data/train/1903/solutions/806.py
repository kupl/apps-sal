class union_find:
    def __init__(self, n):
        self.father = {i:i for i in range(n)}
        self.rank = [1 for i in range(n)]
        self.count = n
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, x, y):
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.rank[x] += self.rank[y]
        self.father[y] = x
        self.count -= 1
    
    def union_andfind(self, x, y):
        father_x, father_y = self.find(x), self.find(y)
        if father_x != father_y:
            self.union(father_x, father_y)
            return False
        return True
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph.append([i, j, cost])
        n = len(points)
        result = 0
        uf = union_find(n)
        for edge in sorted(graph, key = lambda x:x[2]):
            if not uf.union_andfind(edge[0], edge[1]):
                result += edge[2]
        return result
