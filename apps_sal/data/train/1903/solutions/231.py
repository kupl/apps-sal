class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = [[-1 for _ in points] for _ in points]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i][j] = d
                dist[j][i] = d
        if not points or len(points) <= 1:
            return 0
        connected = [False for _ in points]
        min_cost_pq = []
        connected[0] = True
        connected_count = 1
        res = 0
        for j in range(1, len(points)):
            heapq.heappush(min_cost_pq, (dist[0][j], j))
        while connected_count < len(points):
            (d, i) = heapq.heappop(min_cost_pq)
            if connected[i]:
                continue
            res += d
            connected[i] = True
            connected_count += 1
            for j in range(len(points)):
                if not connected[j]:
                    heapq.heappush(min_cost_pq, (dist[i][j], j))
        return res
