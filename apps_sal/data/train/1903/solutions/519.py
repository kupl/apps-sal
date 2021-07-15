class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # a = points
        # n = len(a)
        # def d(i, j): return abs(a[i][0]-a[j][0]) + abs(a[i][1]-a[j][1])
        # q = []
        # dst = [float('inf')]*n
        # vis = [False] * n
        # def consider(du, u):
        #     if vis[u] or du >= dst[u]: return
        #     dst[u] = du
        #     heappush(q, (du, u))
        # consider(0, 0)
        # while q:
        #     du, u = heappop(q)
        #     if vis[u]: continue
        #     vis[u] = True
        #     for v in range(n): consider(d(u, v), v)
        # return sum(dst)
        
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1,n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1]-points[j][1])
                edges.append((d,i,j))
        edges.sort()
        
        roots = [i for i in range(n)]
        
        def find(v):
            if roots[v] != v:
                roots[v] = find(roots[v])
            return roots[v]
        
        def union(u,v):
            p1 = find(u)
            p2 = find(v)
            if p1 != p2:
                roots[p2] = roots[p1]
                return True
            return False
        
        res = 0
        for d,u,v in edges:
            if union(u,v):
                res += d
        return res

