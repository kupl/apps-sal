class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        graph = {'vertices': [], 'edges': []}
        for i1 in range(len(points)):
            graph['vertices'].append(i1)
            for i2 in range(i1 + 1, len(points)):
                if i1 != i2:
                    p1 = points[i1]
                    p2 = points[i2]
                    graph['edges'].append((abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), i1, i2))
        parent = dict()
        rank = dict()

        def make_set(vertice):
            parent[vertice] = vertice
            rank[vertice] = 0

        def find(vertice):
            if parent[vertice] != vertice:
                parent[vertice] = find(parent[vertice])
            return parent[vertice]

        def union(vertice1, vertice2):
            x = find(vertice1)
            y = find(vertice2)
            if rank[x] > rank[y]:
                parent[y] = x
            elif rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
                rank[y] += 1

        def kruskal(graph):
            ans = 0
            edges = sorted(graph['edges'])
            for vertice in graph['vertices']:
                make_set(vertice)
            for edge in edges:
                (weight, vertice1, vertice2) = edge
                if find(vertice1) != find(vertice2):
                    union(vertice1, vertice2)
                    ans += edge[0]
            return ans
        return kruskal(graph)
