class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for i, j, w in edges:
            graph[i].append((j, w))
            graph[j].append((i, w))

        result = []
        for i in range(n):
            queue = [(0, i)]
            distances = defaultdict(lambda: distanceThreshold)
            visited = set()
            while queue:
                distance, i = heapq.heappop(queue)
                if i in visited:
                    continue
                visited.add(i)
                for j, w in graph[i]:
                    new_distance = distance + w
                    if new_distance <= distances[j] and j not in visited:
                        distances[j] = new_distance
                        heapq.heappush(queue, (new_distance, j))
            result.append(len(visited))
        return min(list(range(n)), key=lambda x: (result[x], -x))
