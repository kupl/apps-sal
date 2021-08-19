class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find_parent(parent, x):
            if parent[x] == -1:
                return x
            return find_parent(parent, parent[x])

        def union(parent, x, y):
            x_s = find_parent(parent, x)
            y_s = find_parent(parent, y)
            parent[x_s] = y_s

        def kruskals(edges):
            parent = [-1] * len(points)
            min_weight = 0
            i = 0
            j = 0
            while j < len(points) - 1:
                (start, end, weight) = edges[i]
                x = find_parent(parent, start)
                y = find_parent(parent, end)
                i += 1
                if x != y:
                    j += 1
                    union(parent, x, y)
                    min_weight += weight
            return min_weight
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([i, j, dis])
        edges.sort(key=lambda x: x[2])
        return kruskals(edges)
