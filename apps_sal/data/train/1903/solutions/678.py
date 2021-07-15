from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        self.parent = {}
        self.count = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(heap, (dist, i, j))
                
        result = 0
        while heap:
            cur_dist, point1, point2 = heappop(heap)
            point1_parent = self.find(point1)
            point2_parent = self.find(point2)
            if point1_parent == point2_parent:
                continue
            self.parent[point1_parent] = point2_parent
            self.count[point2_parent] += self.count[point1_parent]
            result += cur_dist
            if self.count[point2_parent] == len(points):
                return result
        return 0
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.count[x] = 1
            return self.parent[x]
        if x == self.parent[x]:
            return self.parent[x]
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
