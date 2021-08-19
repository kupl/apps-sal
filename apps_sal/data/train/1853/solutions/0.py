class Solution:

    def findTheCity(self, n, edges, threshold):
        adj = [[] for _ in range(n)]
        for (u, v, w) in edges:
            adj[u].append((w, v))
            adj[v].append((w, u))
        ans = mn = 100
        for x in range(n):
            cur = 1
            vis = {x}
            dist = [threshold + 1] * n
            hp = [(0, x)]
            while hp:
                (d, u) = heappop(hp)
                if d > dist[u]:
                    continue
                for (w, v) in adj[u]:
                    if d + w < dist[v]:
                        vis.add(v)
                        dist[v] = d + w
                        heappush(hp, (d + w, v))
            if len(vis) <= mn:
                mn = len(vis)
                ans = x
        return ans
