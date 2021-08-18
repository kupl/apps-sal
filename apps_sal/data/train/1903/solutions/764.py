class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i].append((j, d))
                dist[j].append((i, d))
        ret = 0
        visited = set([])
        pq = [(0, 0)]
        while pq:
            w, u = heapq.heappop(pq)
            if u not in visited:
                ret += w
                visited.add(u)
                for v, d in dist[u]:
                    if v not in visited:
                        heapq.heappush(pq, (d, v))
        return ret
