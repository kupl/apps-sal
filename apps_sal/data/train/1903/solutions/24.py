class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = [i for i in range(len(points))]
        
        pq = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x, y = points[i], points[j]
                heapq.heappush(pq, (abs(x[0] - y[0]) + abs(x[1] - y[1]), i, j))
        
        res = 0
        while pq:
            dist, i, j = heapq.heappop(pq)
            if self.find(i, parents) == self.find(j, parents):
                continue
            # print(i, j, dist)
            res += dist
            self.union(i, j, parents)
        
        return res
    
    def find(self, p, parents):
        while p != parents[p]:
            parents[p] = parents[parents[p]]
            p = parents[p]
        return p
    
    def union(self, p, q, parents):
        p_root = self.find(p, parents)
        q_root = self.find(q, parents)
        if p_root != q_root:
            parents[p_root] = q_root
