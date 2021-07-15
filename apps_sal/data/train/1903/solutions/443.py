import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        \"\"\"
        Prim's Algo - minimum spanning tree
        \"\"\"
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        res, n = 0, len(points)
        heap = [(0, (0, 0))]
        seen = set()
        
        while len(seen) < n:
            w, (u, v) = heapq.heappop(heap)
            if u in seen and v in seen:
                continue
            res += w
            seen.add(v)
            for j in range(n):
                if j not in seen and j != v:
                    heapq.heappush(heap, (manhattan(points[v], points[j]), (v, j)))
        
        return res
