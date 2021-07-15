class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(u):
            if u != group[u]:
                group[u] = find(group[u])
            return group[u]
        
        def unite(u, v):
            u, v = find(u), find(v)
            if u == v:
                return False
            if sz[u] < sz[v]:
                u, v = v, u
            group[v] = u
            sz[u] += sz[v]
            return True
        
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges.sort()
        
        ans = 0
        group = [i for i in range(len(points))]
        sz = [1 for i in range(len(points))]
        for e, u, v in edges:
            if unite(u, v):
                ans += e
        return ans

