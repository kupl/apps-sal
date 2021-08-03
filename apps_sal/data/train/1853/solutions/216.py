class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for i, j, w in edges:
            graph[i].append((j, w))
            graph[j].append((i, w))

        result = []
        for i in range(n):
            queue = [(0, i)]
            visited = set()
            while queue:
                distance, i = heapq.heappop(queue)
                if i in visited:
                    continue
                visited.add(i)
                for j, w in graph[i]:
                    if distance + w <= distanceThreshold:
                        heapq.heappush(queue, (distance + w, j))
            visited.remove(i)
            result.append(list(visited))
        return min(range(n), key=lambda x: (len(result[x]), -x))
