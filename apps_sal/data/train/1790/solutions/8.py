class Graph():

    def __init__(self, vertices_num):
        self.v = vertices_num

    # from adjacency matrix to dictionary
    def adjmat_2_graph(self, adjm):
        if len(adjm) != self.v: return "Dimension error"
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

    # from dictionary to adjacency matrix
    def graph_2_mat(self, graph):
        result = [[0] * self.v for _ in range(self.v)]
        for k, links in graph.items():
            for n, d in links:
                result[int(k[1:])][int(n[1:])] = d
        return result

    # from dictionary to adjacency list
    def graph_2_list(self, graph):
        return list(map(list, sorted(graph.items())))

    # from adjacency list to dictionary
    def list_2_graph(self, lst):
        return {k: a for k, a in lst}

    # from adjacency matrix to adjacency list
    def mat_2_list(self, mat):
        return self.graph_2_list(self.adjmat_2_graph(mat))

    # from adjacency list to adjacency matrix
    def list_2_mat(self, lst):
        return self.graph_2_mat(self.list_2_graph(lst))

    # find all path from node start_vertex to node end_vertex
    def find_all_paths(self, graph, start_vertex, end_vertex):
        pths = []; st = [[start_vertex]]
        while st:
            top = st.pop()
            if top[-1] == end_vertex:
                pths.append('-'.join(top))
                continue
            for n, _ in graph[top[-1]]:
                if n not in top:
                    st.append(top + [n])
        return sorted(sorted(pths), key=len)
