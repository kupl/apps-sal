class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        output = []

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        queue = deque([])
        for i in range(n):

            #distance , node
            queue.append((i, 0))

            # current represent a hash map of all of the cities and
            # their distances from i
            curr = {}

            while queue:
                node, dist = queue.popleft()

                if node in curr and dist >= curr[node]:
                    continue

                curr[node] = dist

                for nei, newDist in graph[node]:
                    if newDist + dist <= distanceThreshold:
                        queue.append((nei, newDist + dist))

            output.append(len(curr) - 1)
            # print(output)

        for node in reversed(range(len(output))):
            if output[node] == min(output):
                return node
