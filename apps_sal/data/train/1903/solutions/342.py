from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        dist = defaultdict(lambda: defaultdict(int))
        n = len(points)

        if n <= 1:
            return 0
        if n == 2:
            return abs(points[0][0] - points[1][0]) + abs(points[0][1] - points[1][1])

        for i in range(n - 1):
            for j in range(i + 1, n):
                dist[j][i] = dist[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        seen = set()
        start = 0
        seen.add(start)
        heap = []

        for k, v in list(dist[start].items()):
            heapq.heappush(heap, (v, k))

        ans = 0
        while heap:
            if len(seen) == len(points):
                return ans

            d, node = heapq.heappop(heap)
            if node not in seen:
                seen.add(node)
                ans += d
                for k, v in list(dist[node].items()):
                    heapq.heappush(heap, (v, k))
