class Graph:

    def __init__(self, vertices_num):
        self.v = vertices_num
        self.nodes = [f'A{n}' for n in range(vertices_num)]

    def adjmat_2_graph(self, adjm):
        return {self.nodes[src_index]: [(self.nodes[dst_index], weight) for (dst_index, weight) in enumerate(weights) if weight > 0] for (src_index, weights) in enumerate(adjm) if any((weight > 0 for weight in weights))}

    def graph_2_mat(self, graph):
        result = [[0 for _ in range(self.v)] for _ in range(self.v)]
        for (src, edges) in graph.items():
            src_index = self.nodes.index(src)
            for (dst, weight) in edges:
                dst_index = self.nodes.index(dst)
                result[src_index][dst_index] = weight
        return result

    def graph_2_list(self, graph):
        return sorted([[src, edges] for (src, edges) in graph.items()], key=lambda x: x[0])

    def list_2_graph(self, lst):
        return {src: edges for (src, edges) in lst}

    def mat_2_list(self, mat):
        return self.graph_2_list(self.adjmat_2_graph(mat))

    def list_2_mat(self, lst):
        return self.graph_2_mat(self.list_2_graph(lst))

    def find_all_paths(self, graph, start_vertex, end_vertex, seen=None):
        if start_vertex == end_vertex and seen is None:
            return [start_vertex]
        if seen is None:
            seen = set()
        seen = seen | {start_vertex}
        next_options = [dst for (dst, weight) in graph.get(start_vertex, []) if dst not in seen]
        paths = [start_vertex + '-' + path for option in next_options for path in self.find_all_paths(graph, option, end_vertex, seen)]
        if end_vertex in next_options:
            paths.append(start_vertex + '-' + end_vertex)
        return sorted(sorted(paths, key=str), key=len)
