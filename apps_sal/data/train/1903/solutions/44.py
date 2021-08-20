class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        graph = defaultdict(list)
        start = 0
        for src in range(N):
            for dst in range(N):
                wt = abs(points[src][0] - points[dst][0]) + abs(points[src][1] - points[dst][1])
                graph[src].append((dst, wt))
        dist = {}
        heap = [(0, start)]
        while heap:
            (ddist, node) = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = ddist
            for (neighbor, d) in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (d, neighbor))
        return sum(dist.values())
