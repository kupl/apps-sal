class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = collections.defaultdict(dict)
        n = len(points)
        for i in range(n):
            for j in range(i):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                edges[i][j] = d
                edges[j][i] = d
                
                
        ans = 0
        visited = set([0])
        cand = []
        for j in edges[0]:
            heapq.heappush(cand, [edges[0][j], j])
        ans = 0
        while len(visited) < n:
            d, j = heapq.heappop(cand)
            if j not in visited:
                ans += d
                visited.add(j)
                for i in edges[j]:
                    heapq.heappush(cand, [edges[j][i], i])
        return ans
            

