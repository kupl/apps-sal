import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def cost(a, b):
            return abs(a[0] - b[0]) + abs(a[1] -b[1])
        points = list(map(lambda x: (x[0], x[1]), points))
        minDist = {p:float(\"inf\") for p in points}
        
        
        point = points[0]
        connected = set()
        connected.add(point)
        # q = []
        totalCost = 0
        for p in points:
            if p != point:
                minDist[p] = cost(point, p)
        for i in range(1, len(points)):
            minPoint = None
            minCost = float(\"inf\") 
            for p in points:
                if p not in connected and minDist[p] < minCost:
                    minPoint = p
                    minCost = minDist[p]
            connected.add(minPoint)
            totalCost += minCost
            # update min list
            for p in points:
                if p != minPoint:
                    minDist[p] = min(minDist[p], cost(minPoint, p))
        return totalCost
        # heapq.heappush(q, (cost(point, p), p))
                
                
                
        # connected = set()
        # connected.add(point)
        # totalCost = 0
        # while len(q) > 0:
        #     edgeCost, point = heapq.heappop(q)
        #     if point in connected:
        #         continue
        #     connected.add(point)
        #     totalCost += edgeCost
        #     if len(connected) == len(points):
        #         return totalCost
        #     for p in points:
        #         if p != point:
        #             heapq.heappush(q, (cost(point, p), p))
        # return totalCost
