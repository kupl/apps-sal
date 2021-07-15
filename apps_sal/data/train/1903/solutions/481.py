class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rnk = [0] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim
        N = len(points)
        
        def dist(i, j):
            return (
                abs(points[i][0] - points[j][0]) + 
                abs(points[i][1] - points[j][1])
            )
        
        pq = [[dist(0, j), 0, j] for j in range(1, N)]
        heapq.heapify(pq)
        actives = {0}
        ans = 0
        
        while len(actives) != N:
            d, u, v = heapq.heappop(pq)
            if u not in actives or v not in actives:
                ans += d
                node, = {u, v} - actives
                actives.add(node)
                for nei in range(N):
                    if nei not in actives:
                        heapq.heappush(pq, [dist(node, nei), node, nei])
                        
        return ans
        
        # Kruskal 
        N = len(points)
        edges = []
        for u in range(N-1):
            for v in range(u+1, N):
                edges.append([u, v, abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])])
                
        def MST():
            # Kruskals, edges sorted
            dsu = DSU(N)
            ans = 0
            for u, v, w in sorted(edges, key=lambda e: e[2]):
                if dsu.union(u, v):
                    ans += w
            return ans
        
        return MST()

