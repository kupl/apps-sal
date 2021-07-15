class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, -1, 0)]
        seen = set()
        seen.add(-1)
        heapq.heapify(heap)
        cost = 0
        
        def calc_dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        while len(seen) <= len(points):
            c, a, b = heapq.heappop(heap)
            if b in seen:
                continue
            seen.add(b)
            cost += c
            for j in range(len(points)):
                if j not in seen:
                    heapq.heappush(heap, (calc_dist(points[b], points[j]), b, j))
            
        return cost
                
            
            
                
            
        

