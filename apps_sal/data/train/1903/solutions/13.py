class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
                return parent[x]
            
            return x
                
        n = len(points)
                
        parent = list(range(n))
        
        dists = []
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                mand = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(dists, (mand, i, j))
                
        # dists.sort(key=lambda item: item[0])
        
        res = 0
        
        while dists:
            w, a, b = heapq.heappop(dists)
            pa = find(a)
            pb = find(b)
            
            if pa != pb:
                res += w
                parent[pa] = parent[pb]
                    
        return res
