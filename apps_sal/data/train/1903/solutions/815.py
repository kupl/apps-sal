class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        # G(E,V) has no cycle
        # total |E| is min
        
        def union(u, v):
            parent[find(u)] = parent[find(v)]
        
        def find(v):
            if parent[v] == v:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        parent = {i: i for i in range(len(p))}
        edges = [(abs(p[u][0]-p[v][0])+abs(p[u][1]-p[v][1]), u, v) for u in range(len(p)) for v in range(u + 1, len(p))]
        edges.sort()
        ret = 0
        for d, u, v in edges:
            if find(u) == find(v):
                continue
            union(u, v)
            ret += d
        return ret
