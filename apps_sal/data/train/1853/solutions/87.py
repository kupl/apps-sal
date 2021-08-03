class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        output = []
        queue = deque([])

        for i in range(n):

            queue.append((i, 0))
            curr = {}

            while queue:

                node, dist = queue.popleft()

                if node in curr and dist >= curr[node]:
                    continue

                curr[node] = dist

                for nei, newDist in graph[node]:
                    if dist + newDist <= distanceThreshold:
                        queue.append((nei, dist + newDist))

            output.append(len(curr) - 1)

        for node in reversed(range(len(output))):
            if output[node] == min(output):
                return node
