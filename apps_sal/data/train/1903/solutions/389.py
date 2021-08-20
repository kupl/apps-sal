from collections import defaultdict
import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((cost, j))
                graph[j].append((cost, i))
        seen = [0] * (len(points) + 1)
        seen[0] = 1
        q = graph[0]
        minimumCost = 0
        connectedNodes = 1
        heapq.heapify(q)
        while q:
            (cost, city) = heapq.heappop(q)
            if not seen[city]:
                seen[city] = 1
                minimumCost += cost
                connectedNodes += 1
                for (connectingCost, neighbour) in graph[city]:
                    heapq.heappush(q, (connectingCost, neighbour))
            if connectedNodes >= len(points):
                break
        return minimumCost
