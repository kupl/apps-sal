class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            x0, y0 = points[i]
            for j in range(i + 1, n):
                x1, y1 = points[j]
                d = abs(x0 - x1) + abs(y0 - y1)
                g[i].append((d, j))
                g[j].append((d, i))
        import heapq

        def prim_heap(edge):
            used = [True] * n
            edgelist = []
            for e in edge[0]:
                heapq.heappush(edgelist, e)
                used[0] = False
            res = 0
            while len(edgelist) != 0:
                minedge = heapq.heappop(edgelist)
                if not used[minedge[1]]:
                    continue
                v = minedge[1]
                used[v] = False
                for e in edge[v]:
                    if used[e[1]]:
                        heapq.heappush(edgelist, e)
                res += minedge[0]
            return res
        res = prim_heap(g)
        return res
