class Solution:
    def minCostConnectPoints(self, points) -> int:
        pq = []
        N = len(points)
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        p = list(range(N))
        s = [1] * N
        
        def find(u):
            while u != p[u]:
                p[u] = p[p[u]]
                u = p[u]
            return p[u]
        
        for i in range(N):
            for j in range(i + 1, N):
                heappush(pq, [dist(points[i], points[j]), i, j])
        
        edges = 0
        res = 0
        while edges < N - 1:
            d, u, v = heappop(pq)
            pu, pv = find(u), find(v)
            if pu == pv:
                continue
            edges += 1
            res += d
            if s[pv] > s[pu]:
                pu, pv = pv, pu
            p[pv] = pu
            s[pu] += s[pv]
        return res
