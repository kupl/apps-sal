class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        connections = []
        for i in range(N):
            for j in range(i+1, N):
                connections.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])
        
        if len(connections) < N - 1:
            return -1
        elif N == 1:
            return 0
        uf = {}
        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            uf[find(x)] = find(y)
        
        res = 0
        for start, end, cost in sorted(connections, key=lambda x : x[2]):
            if find(start) != find(end):
                res += cost
                union(start, end)
        if len({find(c) for c in uf}) == 1:
            return res
        return -1

