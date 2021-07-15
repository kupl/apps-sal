class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        distance = []
        for i in range(N):
            for j in range(i + 1, N):
                dist= abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distance.append((dist, i, j))
        heapq.heapify(distance)
        
        parent = [i for i in range(N)]
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        res = 0
        while distance:
            dist, i, j = heapq.heappop(distance)
            pi = find(i)
            pj = find(j)
            if pi != pj:
                parent[pi] = pj
                res += dist
        
        return res
