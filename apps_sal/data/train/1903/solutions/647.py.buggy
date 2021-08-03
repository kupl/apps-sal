class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return self.minCost(points)
    
    
    def minCost(self, points):
        \"\"\"
        
        mst approach
        
        \"\"\"
        n=len(points)
        mst = {0}
        nodes = {idx:cod for idx, cod in enumerate(points)}
        dist = lambda x,y: abs(x[0]-y[0])+abs(x[1]-y[1])
        edges =[]
        for u in range(n): # outdegree of u -- outdegree*heappush time
            heapq.heappush(edges, (dist(nodes[0], nodes[u]), u))
        
        minCostConnect = 0
        while edges:
            far, v = heapq.heappop(edges)
            if v in mst:
                continue
            minCostConnect+=far
            mst.add(v)
            for v_ in range(n):
                if v_ not in mst:
                    heapq.heappush(edges, (dist(nodes[v], nodes[v_]), v_))
        return minCostConnect
