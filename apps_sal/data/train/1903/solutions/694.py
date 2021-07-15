class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        G = collections.defaultdict(list)
        
        for i in range(N):
            for j in range(N):
                if i == j: continue
                cost_x = abs(points[i][0] - points[j][0])
                cost_y = abs(points[i][1] - points[j][1])
                
                cost = cost_x + cost_y
                
                G[i].append((cost, j))
                G[j].append((cost, i))
                
        PQ = []
        SEEN = set()
        
        def add(u):
            SEEN.add(u)
            
            for cost, v in G[u]:
                if v in SEEN:
                    continue
                heapq.heappush(PQ, (cost, v))
                
        mst = 0
        add(0)
        
        while PQ and len(SEEN) < N:
            cost, u = heapq.heappop(PQ)
            if u in SEEN:
                continue
            mst += cost
            add(u)
            
        return mst
