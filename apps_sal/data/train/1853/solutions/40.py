import heapq


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = []
        for _ in range(n):
            graph.append([float('inf')] * n)

        for i, j, w in edges:
            graph[i][j] = w
            graph[j][i] = w

        nums = []
        for i in range(n):
            ans = self.dijkstra(graph, i, distanceThreshold)
            nums.append(ans)

        ans = 0
        minW = float('inf')
        for i, w in enumerate(nums):
            if w <= minW:
                minW = w
                ans = i
        return ans

    def dijkstra(self, graph, idx, threshold):
        dist = [(w, i) for i, w in enumerate(graph[idx]) if w != float('inf')]
        heapq.heapify(dist)
        ans = []
        visited = {idx}
        while len(dist) > 0 and dist[0][0] <= threshold and len(visited) <= len(graph):
            cur_w, i = heapq.heappop(dist)
            if i not in visited:
                ans.append(i)
                visited.add(i)
                for j, w in enumerate(graph[i]):
                    if w != float('inf'):
                        heapq.heappush(dist, (w + cur_w, j))
        return len(ans)
