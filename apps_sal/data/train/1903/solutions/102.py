from heapq import heappop, heappush, heapify


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = [[] for i in range(len(points))]

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        start_point = 0
        min_edge = 1000000000
        for (i, p_i) in enumerate(points[:-1]):
            for (j, p_j) in enumerate(points[i + 1:], i + 1):
                d = dist(p_i, p_j)
                graph[i].append((j, d))
                graph[j].append((i, d))
                if d < min_edge:
                    min_edge = d
                    start_point = i
        total_dist = 0
        pq = [(d, n) for (n, d) in graph[start_point]]
        heapify(pq)
        visited = [False] * len(points)
        visited[start_point] = True
        while len(pq) > 0:
            (d, node) = heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            total_dist += d
            for (child, child_d) in graph[node]:
                if visited[child]:
                    continue
                heappush(pq, (child_d, child))
        return total_dist
