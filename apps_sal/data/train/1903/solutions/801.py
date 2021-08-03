class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        root = {}
        rank = {}

        def make():
            for each_point in points:
                root[tuple(each_point)] = tuple(each_point)
                rank[tuple(each_point)] = 0

        def find(node):
            if node == root[node]:
                return node
            root[node] = find(root[node])
            return root[node]

        def union(a, b):
            p_a, p_b = find(a), find(b)
            if p_a != p_b:
                if rank[p_a] >= rank[p_b]:
                    root[p_b] = p_a
                    if rank[p_a] == rank[p_b]:
                        rank[p_a] += 1
                else:
                    root[p_a] = p_b
                return 1
            else:
                return 0

        L = len(points)
        make()
        edges = []
        for i in range(L):
            for j in range(i + 1, L):
                x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
                edges.append([(x1, y1), (x2, y2), abs(x1 - x2) + abs(y1 - y2)])
        edges.sort(key=lambda x: x[2])
        count, cost = 0, 0
        for edge in edges:
            a, b, c = edge[0], edge[1], edge[2]
            if union(a, b):
                count += 1
                cost += c
            if count == L - 1:
                break
        return cost
