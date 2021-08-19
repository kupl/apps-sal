class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        vertices_with_no_incoming_edges = []
        stack = deque()
        indegree_graph = defaultdict(int)
        vertices_part_of_cycle = []
        no_of_vertices = len(graph)
        for i in range(no_of_vertices):
            indegree_graph[i] = 0
        for source in range(no_of_vertices):
            for dest in graph[source]:
                adj_list[dest].append(source)
                indegree_graph[source] += 1
        for (key, val) in indegree_graph.items():
            if indegree_graph[key] == 0:
                stack.append(key)
                vertices_with_no_incoming_edges.append(key)
        while stack:
            vert = stack.pop()
            if vert in adj_list:
                for v in adj_list[vert]:
                    indegree_graph[v] -= 1
                    if indegree_graph[v] == 0:
                        vertices_with_no_incoming_edges.append(v)
                        stack.append(v)
        return sorted(vertices_with_no_incoming_edges)
