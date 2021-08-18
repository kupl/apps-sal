class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return self.MSTprim(points)

    def MSTkruskal(self, points):
        X = dict()
        R = dict()

        def make_set(point):
            X[point] = point
            R[point] = 0

        def find(point):
            if X[point] != point:
                X[point] = find(X[point])
            return X[point]

        def merge(point1, point2):
            r1 = find(point1)
            r2 = find(point2)
            if r1 != r2:
                if R[r1] > R[r2]:
                    X[r2] = r1
                else:
                    X[r1] = r2
                    if R[r1] == R[r2]:
                        R[r2] += 1

        def kruskal(graph):
            for vertex in graph['vertices']:
                make_set(vertex)

            k_tree = set()

            edges = graph['edges']
            edges.sort()

            for weight, vertex1, vertex2 in edges:
                if find(vertex1) != find(vertex2):
                    merge(vertex1, vertex2)
                    k_tree.add((weight, vertex1, vertex2))

            return k_tree

        N = len(points)
        graph = {'vertices': list(range(N)), 'edges': list()}
        for i in graph['vertices']:
            for j in graph['vertices']:
                if i != j:
                    graph['edges'].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        return sum(weight for weight, _, _ in kruskal(graph))

    def MSTprim(self, points):

        def prim(origin_vertex, edges):
            adjacent_vertex = defaultdict(list)

            for weight, vertex1, vertex2 in edges:
                adjacent_vertex[vertex1].append((weight, vertex1, vertex2))

            p_tree = []
            chosed = set([origin_vertex])

            adjacent_vertexs_edges = adjacent_vertex[origin_vertex]

            heapify(adjacent_vertexs_edges)

            while adjacent_vertexs_edges:
                weight, vertex1, vertex2 = heappop(adjacent_vertexs_edges)

                if vertex2 not in chosed:
                    chosed.add(vertex2)

                    p_tree.append((vertex1, vertex2, weight))

                    for next_vertex in adjacent_vertex[vertex2]:
                        if next_vertex[2] not in chosed:
                            heappush(adjacent_vertexs_edges, next_vertex)

            return p_tree

        N = len(points)
        graph = {'vertices': list(range(N)), 'edges': list()}
        for i in graph['vertices']:
            for j in graph['vertices']:
                if i != j:
                    graph['edges'].append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        return sum(weight for _, _, weight in prim(graph['vertices'][0], graph['edges']))
