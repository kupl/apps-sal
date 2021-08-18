class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        res = 0, math.inf
        for i in range(n):
            visited = set()
            q = []
            heappush(q, (0, i))
            cities = 0
            while q:
                current_weight, node = heappop(q)
                if node in visited:
                    continue
                visited.add(node)
                cities += 1
                for neighbor, neighbor_weight in graph[node]:
                    if neighbor not in visited and current_weight + neighbor_weight <= distanceThreshold:
                        heappush(q, (current_weight + neighbor_weight, neighbor))

            if cities - 1 <= res[1]:
                res = i, cities - 1

        return res[0]
