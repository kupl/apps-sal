class Graph():

    def __init__(self, vertices_num):
        self.v = vertices_num
        self.nodes = None

    def adjmat_2_graph(self, adjm):
        g = {f'A{x}': [] for x in range(self.v)}
        for i in range(self.v):
            for j in range(self.v):
                if adjm[i][j] != 0:
                    g[f'A{i}'].append((f'A{j}', adjm[i][j]))
        return g

    def graph_2_mat(self, graph):
        m = [[0 for j in range(self.v)] for i in range(self.v)]
        for x in range(self.v):
            for g in graph[f'A{x}']:
                m[x][int(g[0][1:])] = g[1]
        return m

    def graph_2_list(self, graph):
        return sorted([[key, val]for key, val in list(graph.items())])

    def list_2_graph(self, lst):
        return {el[0]: el[1] for el in lst}

    def mat_2_list(self, mat):
        return self.graph_2_list(self.adjmat_2_graph(mat))

    def list_2_mat(self, lst):
        return self.graph_2_mat(self.list_2_graph(lst))

    def find_all_paths(self, graph, start_vertex, end_vertex):
        paths = [[start_vertex]]
        new_paths = []
        res = []
        if start_vertex == end_vertex:
            return [start_vertex]
        while paths:
            for p in paths:
                for t in graph[p[-1]]:
                    if t[0] == end_vertex:
                        res.append("-".join(p + [t[0]]))
                        continue
                    if t[0] in p:
                        continue
                    else:
                        new_paths.append(p + [t[0]])
            paths.clear()
            paths, new_paths = new_paths, paths
        return res
