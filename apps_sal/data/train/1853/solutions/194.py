class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = defaultdict(list)
        output = []

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        for i in range(n):

            queue = [(0, i)]
            curr = {}

            while queue:
                dist, node = heapq.heappop(queue)

                if node in curr and dist >= curr[node]:
                    continue

                curr[node] = dist

                for city, distance in graph[node]:
                    if distance + dist <= distanceThreshold:
                        heapq.heappush(queue, (distance + dist, city))

            output.append(len(curr) - 1)

        for i in range(len(output) - 1, -1, -1):
            if output[i] == min(output):
                return i
