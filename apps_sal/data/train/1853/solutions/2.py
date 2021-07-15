class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:             
        graph = {i: [] for i in range(n)}
        # a. create our bidirectional graph with the weights
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        # b. loop over the nodes and retain the minimum cities visited
        res = 0, math.inf
        for i in range(n):
            visited = set()
            q = []
            heappush(q, (0, i))
            cities = 0
            # pop from
            while q:
                current_weight, node = heappop(q)
                if node in visited:
                    continue
                visited.add(node)
                cities += 1
            # loop over neighbors and append only if not visited and weight <= threshold
                for neighbor, neighbor_weight in graph[node]:
                    if neighbor not in visited and current_weight + neighbor_weight <= distanceThreshold:
                        heappush(q, (current_weight + neighbor_weight, neighbor))

            # when the queue is empty, if cities <= res[1]: res = (i, weight)
            if cities - 1 <= res[1]:
                res = i, cities - 1

        return res[0]
