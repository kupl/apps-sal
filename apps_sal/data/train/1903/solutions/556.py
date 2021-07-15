from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        
        helper = lambda pi, pj: abs(pj[0]-pi[0]) + abs(pj[1]-pi[1])
        g = defaultdict(lambda: {}); n = len(p)
        for i in range(n-1):
            for j in range(i+1, n):
                g[i][j] = g[j][i] = helper(p[i], p[j])

        visited = set(); res = 0; pq = []
        heappush(pq, (0, 0)) # u:0, cost:0
        while pq and len(visited) < n:
            cost, u = heappop(pq)
            if u in visited: continue
            res += cost
            for v, w in g[u].items(): heappush(pq, (w, v))
            visited.add(u)
        return res
        
        
    
\"\"\"
[[0,0],[2,2],[3,10],[5,2],[7,0]]
[[3,12],[-2,5],[-4,1]]
[[0,0],[1,1],[1,0],[-1,1]]
[[-1000000,-1000000],[1000000,1000000]]
[[0,0]]
\"\"\"            
