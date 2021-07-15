import heapq

class Solution:
    def minCostConnectPoints(self, P: List[List[int]]) -> int:
        p = P[0]
        q = []
        for x, y in P[1:]:
            d = abs(x - p[0]) + abs(y - p[1])
            heapq.heappush(q, (d, x, y))
            
        seen = {(p[0], p[1])}
        res = 0
        while q:
            d, x, y = heapq.heappop(q)
            if (x, y) in seen:
                continue
            res += d
            seen.add((x, y))
            for x1, y1 in P:
                if (x1, y1) not in seen:
                    d = abs(x1 - x) + abs(y1 - y)
                    heapq.heappush(q, (d, x1, y1))
                    
        return res

