class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(p1, p2):
            (x1, y1) = p1
            (x2, y2) = p2
            return abs(x1 - x2) + abs(y1 - y2)
        import collections
        import heapq
        edges = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    edges.append([i, j, dist(points[i], points[j])])

        def primLazy(edges, n):

            def visit(v):
                included[v] = True
                for neighbor in G[v]:
                    if not included[neighbor]:
                        heapq.heappush(pq, [G[v][neighbor], v, neighbor])
            G = collections.defaultdict(dict)
            for (v, w, weight) in edges:
                G[v][w] = weight
                G[w][v] = weight
            included = [False for i in range(n)]
            mst = []
            pq = []
            visit(points[0])
            d = 0
            while pq:
                (dist, v, w) = heapq.heappop(pq)
                if included[v] and included[w]:
                    continue
                mst.append([v, w])
                d += G[v][w]
                if not included[v]:
                    visit(v)
                if not included[w]:
                    visit(w)
            return mst

        def kruskalSize(edges, n):
            parent = [i for i in range(n)]
            sz = [1 for i in range(n)]

            def find(i):
                while i != parent[i]:
                    i = parent[i]
                return i

            def union(x, y):
                (rx, ry) = (find(x), find(y))
                if rx == ry:
                    return
                if sz[rx] < sz[ry]:
                    parent[rx] = ry
                    sz[ry] += sz[rx]
                else:
                    parent[ry] = rx
                    sz[rx] += sz[ry]
            mst = []
            d = 0
            edges = sorted(edges, key=lambda x: x[2])
            for (v, w, weight) in edges:
                if find(v) != find(w):
                    mst.append([v, w])
                    d += weight
                    union(v, w)
            return d
        return kruskalSize(edges, len(points))
