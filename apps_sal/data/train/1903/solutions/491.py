from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        g = defaultdict(lambda: {}); n = len(points)
        for i in range(n-1):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, n):
                x2, y2 = points[j][0], points[j][1]
                val = abs(x2-x1) + abs(y2-y1)
                g[i][j] = g[j][i] = val

                
        visited = set(); res = 0; q = []; cnt=0
        heappush(q, (0, 0)) # u:0, cost:0
        while q:
            cost, u = heappop(q)
            if u in visited: continue
            res += cost
            cnt += 1
            for v, w in g[u].items():
                heappush(q, (w, v))
            visited.add(u)
            if cnt >= n: break
        return res
        
        
    
\"\"\"
[[0,0],[2,2],[3,10],[5,2],[7,0]]
[[3,12],[-2,5],[-4,1]]
[[0,0],[1,1],[1,0],[-1,1]]
[[-1000000,-1000000],[1000000,1000000]]
[[0,0]]
\"\"\"            
