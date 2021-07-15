class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pointSet = set()
        CostHeap = []
        
        for i in range(len(points)):
            pointSet.add(i)
            for j in range(i+1, len(points)):
                heapq.heappush(CostHeap, [abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), i, j])
        
        parent = defaultdict(lambda: -1)
        def find(x):
            if parent[x] == -1:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]
            
        COST = 0
        while CostHeap:
            node = heapq.heappop(CostHeap)
            cost,x,y = node
            u = find(x)
            v = find(y)
            if u != v:
                parent[u] = v               
                COST+=cost
        return COST
            

