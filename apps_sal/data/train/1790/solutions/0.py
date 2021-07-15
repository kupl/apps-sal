from collections import deque
class Graph():

    def __init__(self, vertices_num):
        self.v = vertices_num

    def adjmat_2_graph(self, adjm):
        d = {f'A{i}': [] for i in range(self.v)}
        for i, j in enumerate(adjm):
            for k, l in enumerate(j):
                if l : d[f'A{i}'].append((f'A{k}', l))
        return d

    def graph_2_mat(self, graph):
        mat = [[0 for _ in range(self.v)] for _ in range(self.v)]
        for i, j in graph.items():
            for k, l in j:
                mat[int(i[1])][int(k[1])] = l
        return mat

    def graph_2_list(self, graph):
        return [[i, j] for i, j in sorted(graph.items())]

    def list_2_graph(self, lst):
        return {i: x for i, x in lst}

    def mat_2_list(self, mat):
        return self.graph_2_list(self.adjmat_2_graph(mat))

    def list_2_mat(self, lst):
        return self.graph_2_mat(self.list_2_graph(lst))

    def find_all_paths(self, graph, start, end):
        graph = {i: [k[0] for k in j] for i, j in graph.items()}
        Q, paths = deque([[start, []]]), []
        while Q:
            node, path = Q.popleft()
            path.append(node)

            if node == end:
                paths.append('-'.join(path))

            for n in graph[node]:
                if n not in path:
                    Q.append([n, path[:]])
        return sorted(paths, key=len)
