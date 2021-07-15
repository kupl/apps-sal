class Solution:
    def find(self, pt):
        if pt == self.roots[pt]:
            return pt
        self.roots[pt] = self.find(self.roots[pt])
        return self.roots[pt]
    
    def union(self, p1, p2):
        parent1, parent2 = self.find(p1), self.find(p2)
        if parent1 == parent2:
            return False
        if self.rank[parent2] < self.rank[parent1]:
            parent1, parent2 = parent2, parent1
            p1, p2 = p2, p1
        if self.rank[parent1] == self.rank[parent2]:
            self.rank[parent2] += 1
        self.roots[parent1] = parent2
        # self.find(p1)
        # self.find(p2)
        return True
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.roots = {(x, y): (x, y) for (x, y) in points}
        self.rank = {(x, y): 0 for (x, y) in points}
        ans = 0
        edges = []
        for i in range(len(points)):
            p1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                p2 = points[j][0], points[j][1]
                # if p1 != p2:
                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edges.append((dist, p1, p2))
        edges.sort()
        for dist, p1, p2 in edges:
            if self.union(p1, p2):
                ans += dist
        return ans
        
        # for i in range(len(points)):
        #     x1, y1 = points[i]
        #     best = (float('inf'), (x1, y1))
        #     for j in range(len(points)):
        #         if i == j:
        #             continue
        #         x2, y2 = points[j]
        #         dist = abs(x1-x2) + abs(y1-y2)
        #         best = min(best, (dist, (x2, y2)))
        #     p1 = x1, y1
        #     dist, p2 = best
        #     if self.union(p1, p2):
        #         print(\"connecting {}, {} distance {}\".format(p1, p2, dist))
        #         ans += dist
        # return ans

