class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        connected, dis = set(), [float(\"inf\")] * n
        
        res = 0
        cur = nxt = 0
        d = dis[0]
        
        for _ in range(n-1):
            
            connected.add(cur)
            xx, yy = points[cur]
            
            for j, (x, y) in enumerate(points):
                if j in connected: continue
                    
                dis[j] = min(dis[j], abs(x - xx) + abs(y - yy))
                
                if dis[j] < d:
                    nxt, d = j, dis[j]
            
            res += d
            cur = nxt
            d = float(\"inf\")
            
        return res
