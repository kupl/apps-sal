class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        result = {} 

        # build the adjacency list
        for edge in edges:
            src = edge[0]
            dest = edge[1]
            cost = edge[2]

            graph[src].append((dest, cost))
            graph[dest].append((src, cost))

        # {0: [(1, 3)], 1: [(2, 1), (3, 4)], 2: [(3, 1)]}
        # get the number of vertices that can be reached starting from vertex i. Also, the vertices
        # that can be reached should have a distance below the threshold.
        for i in range(n): # 0
            num_vertices = self.get_num_vertices_less_than_threshold(graph, i, distanceThreshold) # g, 0, 4
            result[i] = num_vertices
        
        # pprint.pprint(result)
        min_vertex_val = min(result.values())
        # pprint.pprint(min_vertex_val)

        index = list([-1 if x[1] != min_vertex_val else x[0] for x in list(result.items())])

        # pprint.pprint(index)

        # min_vertex = sorted(result.items(), key=lambda x: x[1])
        # pprint.pprint(min_vertex)

        return max(index)
    
    def get_num_vertices_less_than_threshold(self, graph, vertex, thresh): # g, 0, 4
        queue = [] 
        queue.append((0, vertex)) # (0, 0) 
        reachable_nodes = [] # []

        while queue: # (3, 1)
            dist, node = heapq.heappop(queue) # 3, 1

            if node in reachable_nodes:
                continue
            
            reachable_nodes.append(node) # [0, 1]

            for vert in graph[node]: # (2, 1), (3, 4)
                neigh_vert = vert[0] # 2
                neigh_cost = vert[1] # 1

                if dist + neigh_cost <= thresh: # 3 + 1 <= 4
                    heapq.heappush(queue, (dist + neigh_cost, neigh_vert)) # [(4, 1)]

        return len(reachable_nodes) - 1 

