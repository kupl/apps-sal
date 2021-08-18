class Graph():

    def __init__(self, vertices_num):
        self.v = vertices_num
        self.nodes = None

    def adjmat_2_graph(self, adjm):
        gra = {}
        for vern, i in enumerate(adjm):
            tem = []
            for ind, v in enumerate(i):
                if v != 0:
                    tem.append(('A{}'.format(ind), v))
                    gra['A{}'.format(vern)] = tem
        return gra

    def graph_2_mat(self, graph):
        mat = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
        for k, v in graph.items():
            for i in v:
                mat[int(k[1])][int(i[0][1])] = i[1]

        return mat

    def graph_2_list(self, graph):
        return sorted([[k, v] for k, v in graph.items()], key=lambda x: x[0])

    def list_2_graph(self, lst):
        return {i[0]: i[1] for i in lst}

    def mat_2_list(self, mat):
        lst = []
        for ind, v in enumerate(mat):
            tem = []
            for ind1, i in enumerate(v):
                if i != 0:
                    tem.append(('A{}'.format(ind1), i))
            lst.append(['A{}'.format(ind), tem])
        return sorted(lst, key=lambda x: x[0])

    def list_2_mat(self, lst):
        mat = [[0 for _ in range(len(lst))] for _ in range(len(lst))]
        for i in lst:
            for j in i[1]:
                mat[int(i[0][1])][int(j[0][1])] = j[1]
        return mat

    def find_all_paths(self, graph, start_vertex, end_vertex):
        all_paths = []
        sta = [[start_vertex]]
        while sta:
            a = sta.pop()
            if a[-1] == end_vertex:
                all_paths.append(a)
                continue
            for i in graph[a[-1]]:
                if i[0] not in a:
                    sta.append(a + [i[0]])
        return ['-'.join([i for i in p]) for p in sorted(sorted(all_paths), key=len)]
