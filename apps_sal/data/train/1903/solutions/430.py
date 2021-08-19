class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(u, v):
            return abs(u[0] - v[0]) + abs(u[1] - v[1])
        from collections import defaultdict
        n = len(points)
        graph = defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                w = manhattan(points[i], points[j])
                graph[i].append((w, j))
                graph[j].append((w, i))
        k = 0
        costs = 0
        seen = [False] * n
        heap = [(0, 0)]
        while heap:
            (w, u) = heapq.heappop(heap)
            if not seen[u]:
                seen[u] = True
                costs += w
                k += 1
                if k == n:
                    break
                for (ew, v) in graph[u]:
                    heapq.heappush(heap, (ew, v))
        return costs
