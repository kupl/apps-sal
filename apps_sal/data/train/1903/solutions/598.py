class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def union(g, u, v):
            p = g[u]
            o = g[v]
            for i in g.keys():
                if g[i] == o:
                    g[i] = p                    

        N = len(points)
        matrix = [[float('inf')]*N for _ in range(N)]
        ans = 0
        edges = []
        for node in range(N):
            for neighbor in range(N):
                if node == neighbor: continue
                if matrix[node][neighbor] != float('inf'): continue
                u, v = points[node], points[neighbor]
                d = abs(u[0] - v[0]) + abs(u[1] - v[1])
                matrix[node][neighbor] = d
                matrix[neighbor][node] = d
                edges.append((node, neighbor, d))
                edges.append((neighbor, node, d))
        P = {_: _ for _ in range(N)}
        edges.sort(key=lambda x: x[2])
        for u, v, w in edges:
            if P[u] != P[v]:
                union(P, u, v)
                ans += w
        return ans
