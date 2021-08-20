class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        e = [[] for _ in points]
        n = len(points)
        for (i, u) in enumerate(points):
            for j in range(i + 1, n):
                v = points[j]
                d = abs(u[0] - v[0]) + abs(u[1] - v[1])
                e[i].append((d, j))
                e[j].append((d, i))
        tree = {0}
        pq = []
        for v in e[0]:
            pq.append(v)
        heapify(pq)
        c = 0
        while len(tree) < n:
            try:
                (d, v) = heappop(pq)
            except IndexError:
                break
            if v in tree:
                continue
            c += d
            tree.add(v)
            for u in e[v]:
                heappush(pq, u)
        return c
