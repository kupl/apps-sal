class Solution:
    def _dist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0
        comp = [points[0]]
        h = []
        
        for i in range(1, len(points)):
            heapq.heappush( h, [self._dist(points[0], points[i]), points[i]] )
        
        while h:
            dist, p = heapq.heappop(h)
            result += dist
            
            for i in range(len(h)):
                h[i][0] = min( h[i][0], self._dist(p, h[i][1]) )
            heapq.heapify(h)
        return result
