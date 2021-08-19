class Solution:

    def visitedAllNodes(self, src, graph, n, max_d):
        visited = [False for i in range(n)]
        heap = [(0, src)]
        while heap:
            (d, node) = heapq.heappop(heap)
            if not visited[node]:
                visited[node] = True
                for (neighbor, w) in graph[node]:
                    if d + w <= max_d and (not visited[neighbor]):
                        heapq.heappush(heap, (d + w, neighbor))
        return sum(visited)

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        (node, nodes_reached) = (-1, n + 1)
        for (i, j, w) in edges:
            graph[i].append((j, w))
            graph[j].append((i, w))
        for i in range(n):
            count = self.visitedAllNodes(i, graph, n, distanceThreshold)
            if count <= nodes_reached:
                node = i
                nodes_reached = count
        return node
