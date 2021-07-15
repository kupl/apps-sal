class Graph():
    def __init__(self, vertices_num):
        pass

    # from adjacency matrix to dictionary
    @staticmethod
    def adjmat_2_graph(adjm):
        nodes_dct = {}
        for row, weights in enumerate(adjm):
            edges = [('A'+str(col), w) for col, w in enumerate(weights) if w > 0]
            nodes_dct['A'+str(row)] = edges

        return nodes_dct

    @staticmethod
    def graph_2_mat(graph):
        g_size = len(list(graph.keys()))
        matrix = [[0 for _ in range(g_size)] for _ in range(g_size)]

        for vname, edges in list(graph.items()):
            v = int(vname[1:])
            for e in edges:
                u = int(e[0][1:])
                matrix[u][v] = e[1]

        return matrix

    @staticmethod
    def graph_2_list(graph):
        return [[k, v] for k, v in sorted(graph.items())]

    # from adjacency list to dictionary
    @staticmethod
    def list_2_graph(lst):
        return dict((vertex[0], vertex[1]) for vertex in lst)

    @staticmethod
    def mat_2_list(mat):
        return Graph.graph_2_list(Graph.adjmat_2_graph(mat))

    @staticmethod
    def list_2_mat(lst):
        return Graph.graph_2_mat(Graph.list_2_graph(lst))

    @staticmethod
    def find_all_paths(graph, start_vertex, end_vertex):
        if start_vertex == end_vertex:
            return [start_vertex]

        paths = []
        def find(path):
            for e in graph[path[-1]]:
                v = e[0]
                if v not in path:
                    new_path = path[:] + [v]
                    if v == end_vertex:
                        paths.append(new_path)
                    else:
                        find(new_path)

        find([start_vertex])

        l = list(['-'.join(p) for p in paths])
        return sorted(sorted(l, key=str), key=len)

