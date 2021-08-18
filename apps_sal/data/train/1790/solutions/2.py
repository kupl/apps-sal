class Graph():

    def __init__(self, vertices_num):
        self.v = vertices_num

    def sort_adj_list(self, lst):
        res = []
        for l in lst:
            res.append([l[0], sorted(l[1])])
        return sorted(res)

    def adjmat_2_graph(self, adjm):
        if len(adjm) != self.v:
            return "Dimension error"
        nodes = ['A' + str(i) for i in range(0, self.v)]
        graph = {}
        for n, v in enumerate(nodes):
            voisin = []
            for i, dist in enumerate(adjm[n]):
                if dist != 0:
                    voisin.append((nodes[i], dist))
            graph[v] = voisin
        self.graph = graph
        return graph

    def graph_2_mat(self, graph):
        nodes = sorted(graph.keys())
        adjm = []
        for node in nodes:
            L = [0] * len(nodes)
            parcours = graph[node]
            for voisin, dist in parcours:
                L[nodes.index(voisin)] = dist
            adjm.append(L)
        return adjm

    def graph_2_list(self, graph):
        r = [[k, graph[k]] for k in sorted(graph.keys())]
        return self.sort_adj_list(r)

    def list_2_graph(self, lst):
        if len(lst) != self.v:
            return "Dimension error"
        dct = {}
        for l in lst:
            dct[l[0]] = l[1]
        return dct

    def mat_2_list(self, mat):
        if len(mat) != self.v:
            return "Dimension error"
        return self.graph_2_list(self.adjmat_2_graph(mat))

    def list_2_mat(self, lst):
        if len(lst) != self.v:
            return "Dimension error"
        return self.graph_2_mat(self.list_2_graph(lst))

    def find_all_paths_aux(self, start, end, path=[]):
        graph = self.graph
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for vertex in list([x[0] for x in graph[start]]):
            if vertex not in path:
                extended_paths = self.find_all_paths_aux(vertex, end, path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def find_all_paths(self, graph, start, end):
        self.graph = graph
        paths = self.find_all_paths_aux(start, end)
        paths = list(["-".join(x) for x in paths])
        return sorted(sorted(paths, key=str), key=len)
