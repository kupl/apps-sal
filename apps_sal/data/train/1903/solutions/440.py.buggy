class Solution:
    \"\"\"MST
    778. swim-in-rising-water
    787. cheapest-flights-within-k-stops
    1102. path-with-maximum-minimum-value
    1135. connecting-cities-with-minimum-cost
    1584. min-cost-to-connect-all-points
    \"\"\"
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def hm(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        g = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = hm(points[i], points[j])
                g[i].append((dist, j))
                g[j].append((dist, i))
        # print(g)
        
        visited = set()
        pq = [(0, 1)]
        res = 0
        while len(visited) < len(points):
            cost, p = heapq.heappop(pq)
            if p not in visited:
                res += cost
                visited.add(p)
                for nei_cost, nei_p in g[p]:
                    heapq.heappush(pq, (nei_cost, nei_p))
        return res
