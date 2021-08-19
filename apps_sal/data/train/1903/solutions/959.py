class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        graph = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if i != j:
                    (x1, y1) = points[i]
                    (x2, y2) = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    graph[i].append((j, dist))
                    graph[j].append((i, dist))
        pq = [(0, 0)]
        visited = set()
        cost = 0
        while len(visited) < N:
            (dist, node) = heappop(pq)
            if node not in visited:
                visited.add(node)
                cost += dist
                for (adj, dist) in graph[node]:
                    if adj not in visited:
                        heappush(pq, (dist, adj))
        return cost
