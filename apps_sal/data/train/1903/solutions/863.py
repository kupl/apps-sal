class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if not points:
            return 0

        cost = 0
        graph = defaultdict(dict)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    graph[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    graph[j][i] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        visited = set()
        graph[-1][0] = 0
        pq = [(0, -1, 0)]
        heapq.heapify(pq)

        while pq:
            if len(visited) == len(points):
                return cost
            edge_cost, u, v = heapq.heappop(pq)
            if v not in visited:
                cost += edge_cost
            visited.add(v)
            for nbr in graph[v]:
                if nbr not in visited:
                    heapq.heappush(pq, (graph[v][nbr], v, nbr))

        return cost
