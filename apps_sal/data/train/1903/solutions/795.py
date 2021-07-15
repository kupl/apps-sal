class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distance = []
        n = len(points)
        for i in range(n):
            for j in range(i, n):
                point_1 = points[i]
                point_2 = points[j]
                dist = abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])
                distance.append((dist, tuple(point_1), tuple(point_2)))
        
        distance = sorted(distance, key=lambda x: x[0])
        points = [tuple(p) for p in points]
        # print(points)
        union_find = UnionFind(points=points)
        ans = 0
        for dist_pair in distance:
            if union_find.is_connected(dist_pair[1], dist_pair[2]):
                continue
            union_find.union(dist_pair[1], dist_pair[2])
            ans += dist_pair[0]
        
        return ans

class UnionFind:
    def __init__(self, points):
        self.father = {p: p for p in points}
    
    def find(self, p):
        if self.father[p] == p:
            return p
        self.father[p] = self.find(self.father[p])
        return self.father[p]
        
    def union(self, p1, p2):
        father_1 = self.find(p1)
        father_2 = self.find(p2)
        if father_1 != father_2:
            self.father[father_1] = father_2
    
    def is_connected(self, p1, p2):
        father_1 = self.find(p1)
        father_2 = self.find(p2)
        if father_1 == father_2:
            return True
        return False
