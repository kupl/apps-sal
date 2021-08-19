import heapq


class Solution:

    def shortestPath(self, root, graph, distanceThreshold):
        dist = {}
        dist[root] = 0
        visited = set()
        queue = [(0, root)]
        count = 0
        while queue:
            (pickDist, pick) = heapq.heappop(queue)
            if pick in visited:
                continue
            visited.add(pick)
            if pickDist <= distanceThreshold:
                count += 1
            else:
                continue
            for (neighbor, weight) in graph[pick]:
                dist[neighbor] = min(dist.get(neighbor, float('inf')), pickDist + weight)
                heapq.heappush(queue, (dist[neighbor], neighbor))
        return count

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = {k: [] for k in range(n)}
        for (u, v, w) in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        minReachableCount = float('inf')
        ans = 0
        for i in range(n):
            reachCount = self.shortestPath(i, graph, distanceThreshold)
            if reachCount <= minReachableCount:
                minReachableCount = reachCount
                ans = i
        return ans
