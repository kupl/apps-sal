class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        import heapq
        
        HQ = []
        
        heapq.heapify(HQ)
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                heapq.heappush(HQ, (dist, i, j))
        
        G = list(range(len(points)))
        
        def find(x):
            if G[x] != x:
                G[x] = find(G[x])
            return G[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            G[x] = y
            return True
        
        res = 0
        while HQ:
            curdist, curi, curj = heapq.heappop(HQ)
            if union(curi, curj):
                res += curdist
        
        return res
