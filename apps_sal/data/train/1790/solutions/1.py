class Graph():

    def __init__(self, vertices_num):
        self.v = vertices_num
        self.nodes = [f"A{i}" for i in range(self.v)]
        self.ids = {x: i for i, x in enumerate(self.nodes)}

    # from adjacency matrix to dictionary
    def adjmat_2_graph(self, adjm):
        return {self.nodes[i]: [(self.nodes[j], x) for j, x in enumerate(row) if x] for i, row in enumerate(adjm)}

    # from dictionary to adjacency matrix
    def graph_2_mat(self, graph):
        result = [[0] * self.v for _ in range(self.v)]
        for i, L in graph.items():
            for j, x in L:
                result[self.ids[i]][self.ids[j]] = x
        return result

    # from dictionary to adjacency list
    def graph_2_list(self, graph):
        return list(map(list, sorted(graph.items())))

    # from adjacency list to dictionary
    def list_2_graph(self, lst):
        return dict(lst)

    # from adjacency matrix to adjacency list
    def mat_2_list(self, mat):
        return self.graph_2_list(self.adjmat_2_graph(mat))

    # from adjacency list to adjacency matrix
    def list_2_mat(self, lst):
        return self.graph_2_mat(self.list_2_graph(lst))

    @staticmethod
    def gen(graph, start, end, seen):
        if start == end:
            yield [end]
        else:
            for k, v in graph[start]:
                if k not in seen:
                    for L in Graph.gen(graph, k, end, seen | {k}):
                        yield [start] + L

    # find all path from node start_vertex to node end_vertex
    def find_all_paths(self, graph, start_vertex, end_vertex):
        return sorted(map('-'.join, Graph.gen(graph, start_vertex, end_vertex, {start_vertex})), key=lambda x: (len(x), x))
