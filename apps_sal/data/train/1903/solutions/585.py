class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        
    def union(self, index1, index2):
        root1 = self.find(index1)
        root2 = self.find(index2)
        if root1 == root2:
            return 0
        elif root1 > root2:
            self.parents[root2] = root1
        else:
            self.parents[root1] = root2
        return 1
    
    def find(self, index):
        if self.parents[index] != index:
            self.parents[index] = self.find(self.parents[index])
        return self.parents[index]

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        
        edges = []
        for i, point1 in enumerate(points):
            for j in range(i + 1, len(points)):
                point2 = points[j]
                distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                edges.append((distance, i, j))
        edges.sort()
        
        uf = UnionFind(len(points))
        total = 0
        for i, (weight, node1, node2) in enumerate(edges):
            is_union = uf.union(node1, node2)
            if is_union:
                total += weight
        return total
        

