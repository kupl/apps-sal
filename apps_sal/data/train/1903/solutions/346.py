class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def distance(u, v): return abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])

        graph = defaultdict(list)
        for u in range(n):
            for v in range(u + 1, n):
                dist = distance(u, v)
                graph[u].append((dist, v))
                graph[v].append((dist, u))

        count = 1
        cost = 0
        visited = [True] + [False] * (n - 1)
        heap = graph[0][:]
        heapify(heap)

        while heap:
            dist, u = heappop(heap)
            if not visited[u]:
                visited[u] = True
                count += 1
                cost += dist
                for link in graph[u]:
                    heappush(heap, link)

            if count >= n:
                break

        return cost
