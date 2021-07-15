class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def dist(points,i,j):
            return abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        visited = [(0,(0,0))]
        ans, n = 0, len(points)
        seen = set()
        
        while len(seen) < n:
            d,(u,v) = heappop(visited)
            if u in seen and v in seen:continue
            ans += d
            seen.add(v)
            for j in range(n):
                if j not in seen and  j != v:
                    heappush(visited, (dist(points,j,v), (v, j)))
        return ans
            

