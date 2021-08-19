class Solution:

    def dijkstra(self, graph, src):
        (dist, visited) = ({}, collections.defaultdict(bool, {src: True}))
        for u in graph:
            dist[u] = float('inf')
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            (cur, city) = heapq.heappop(heap)
            visited[city] = True
            for (to, weight) in graph[city]:
                if not visited[to] and dist[to] > cur + weight:
                    dist[to] = cur + weight
                    heapq.heappush(heap, (dist[to], to))
        return dist

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        for (u, v, w) in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        neighbors = collections.defaultdict(int)
        for city in graph:
            for (c, dist) in list(self.dijkstra(graph, src=city).items()):
                if city != c and dist <= distanceThreshold:
                    neighbors[city] += 1
        for i in range(n):
            if neighbors[i]:
                pass
        (answer, min_neighbors) = (-1, float('inf'))
        for (city, num) in list(neighbors.items()):
            if num < min_neighbors or (num == min_neighbors and city > answer):
                answer = city
                min_neighbors = num
        return answer
