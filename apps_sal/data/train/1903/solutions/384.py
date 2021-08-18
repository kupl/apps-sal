class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        graph = [[0] * len(points) for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i][j] = graph[j][i] = dist
        heap = [(0, 0)]
        asr = 0
        for i in range(len(points)):
            dist, idx = heapq.heappop(heap)
            while heap and idx in visited:
                dist, idx = heapq.heappop(heap)
            visited.add(idx)
            asr += dist
            for v in range(len(points)):
                if v not in visited:
                    heapq.heappush(heap, (graph[idx][v], v))
        return asr
