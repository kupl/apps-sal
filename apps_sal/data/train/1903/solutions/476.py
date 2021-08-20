class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dist = {}
        (pair, mindist) = ((0, 0), math.inf)
        for i in range(N):
            for j in range(i + 1, N):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i, j] = dist[j, i] = d
                if d < mindist:
                    (pair, mindist) = ((i, j), d)
        res = mindist
        mst = set(pair)
        other = set((i for i in range(N) if i not in mst))
        h = []
        for v in mst:
            for i in other:
                heapq.heappush(h, (dist[v, i], i))
        while len(mst) < N:
            (d, i) = heapq.heappop(h)
            if i not in mst:
                res += d
                mst.add(i)
                other.remove(i)
                for j in other:
                    heapq.heappush(h, (dist[i, j], j))
        return res if N > 1 else 0
