class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        result = {}

        for edge in edges:
            src = edge[0]
            dest = edge[1]
            cost = edge[2]

            graph[src].append((dest, cost))
            graph[dest].append((src, cost))

        for i in range(n):
            num_vertices = self.get_num_vertices_less_than_threshold(graph, i, distanceThreshold)
            result[i] = num_vertices

        min_vertex_val = min(result.values())

        index = list([-1 if x[1] != min_vertex_val else x[0] for x in list(result.items())])

        return max(index)

    def get_num_vertices_less_than_threshold(self, graph, vertex, thresh):
        queue = []
        queue.append((0, vertex))
        reachable_nodes = []

        while queue:
            dist, node = heapq.heappop(queue)

            if node in reachable_nodes:
                continue

            reachable_nodes.append(node)

            for vert in graph[node]:
                neigh_vert = vert[0]
                neigh_cost = vert[1]

                if dist + neigh_cost <= thresh:
                    heapq.heappush(queue, (dist + neigh_cost, neigh_vert))

        return len(reachable_nodes) - 1
