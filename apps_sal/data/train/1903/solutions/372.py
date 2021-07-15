class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 1:
            return 0
        dist = {}
        for p in range(1,len(points)):
            dist[p] = abs(points[p][0] - points[0][0]) + abs(points[p][1] - points[0][1])
        print(dist)
        cost = 0
        while dist:
            min_k = 0
            min_v = 1e10
            for k,v in list(dist.items()):
                if v < min_v:
                    min_v = v
                    min_k = k
            print((min_k,min_v))
            cost += min_v
            for k,v in list(dist.items()):
                dist[k] = min(dist[k], abs(points[min_k][0] - points[k][0]) + abs(points[min_k][1] - points[k][1]))
            assert dist[min_k] == 0
            del dist[min_k]
            
        return cost
                

