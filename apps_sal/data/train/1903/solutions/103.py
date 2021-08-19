class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # return self.MSTkruskal(points) # 8504ms
        return self.MSTprim(points)  # 7640 ms

    def MSTkruskal(self, points):
        X = dict()
        R = dict()

        # 初始化并查集
        def make_set(point):
            X[point] = point
            R[point] = 0

        # 找到节点的根
        def find(point):
            if X[point] != point:
                X[point] = find(X[point])
            return X[point]

        # 连接两个节点
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

        # KRUSKAL算法实现
        def kruskal(graph):
            # 遍历顶点，初始化并查集
            for vertex in graph['vertices']:
                make_set(vertex)

            k_tree = set()

            edges = graph['edges']
            # 按照权重从小到大排序
            edges.sort()

            # 遍历每一条边
            for weight, vertex1, vertex2 in edges:
                # 判断两个顶点是否联通：即是否在属于一棵树
                if find(vertex1) != find(vertex2):
                    # 如果未联通，则将其联通
                    merge(vertex1, vertex2)
                    # 加入生成树
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

            # 将edges列表中各项归类成以某点为dictionary的key，其value则是其相邻的点及其权重
            # 形如：{'A': [(7, 'A', 'B'), (5, 'A', 'D')],
            #       'C': [(8, 'C', 'B'), (5, 'C', 'E')]}
            for weight, vertex1, vertex2 in edges:
                adjacent_vertex[vertex1].append((weight, vertex1, vertex2))

            p_tree = []
            # 标记是否已选择：这里首先选择源点
            chosed = set([origin_vertex])

            # 得到与源点直连的相邻点边
            adjacent_vertexs_edges = adjacent_vertex[origin_vertex]

            # 将源点所有的直连边加入小顶堆中
            heapify(adjacent_vertexs_edges)

            # 循环遍历小顶堆
            while adjacent_vertexs_edges:
                # 从堆中取出边权值最小的点信息。
                weight, vertex1, vertex2 = heappop(adjacent_vertexs_edges)

                # 如果边权值最小的对端点还没有加入生成树中
                if vertex2 not in chosed:
                    # 将该点标记已选择
                    chosed.add(vertex2)

                    # 将该最小边加入生成树中
                    p_tree.append((vertex1, vertex2, weight))

                    # 遍历与该点直连的相邻点边
                    for next_vertex in adjacent_vertex[vertex2]:
                        # 如果该点的对端点还没有被选择，则将其对应的边加入堆中
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
