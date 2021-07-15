from pprint import pprint
class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        
        def getMinNode(n, val, mst):
            mn = math.inf
            mn_idx = None
            for i in range(n):
                if (mst[i] == False and val[i] < mn):
                    mn = val[i]
                    mn_idx = i
            return mn_idx
        
        res = 0
        n = len(p)
        parent = [None] * n
        parent[0] = -1
        
        dists = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    dists[i][j] = dists[j][i] = abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1])
        
        # pprint(dists)
        mst = [False] * n
        val = [math.inf] * n
        val[0] = 0
        for i in range(n - 1):
            u = getMinNode(n, val, mst)
            mst[u] = True
            for v in range(n):
                if dists[u][v] and mst[v] == False and dists[u][v] < val[v]:
                    val[v] = dists[u][v]
                    parent[v] = u
        for i in range(1, n):
            # print(dist[parent[i]])
            # print(dist)
            res += dists[parent[i]][i]
        return res
