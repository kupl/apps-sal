from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []

        n = len(points)

        parent = defaultdict(lambda: -1)

        def find_parent(x, y):

            if parent[(x, y)] == -1:
                return x, y

            else:
                parent[(x, y)] = find_parent(*parent[(x, y)])
                return parent[(x, y)]

        def merge(x1, y1, x2, y2):

            if x1 == x2 and y1 == y2:
                return

            parent_of_i = find_parent(x1, y1)
            parent_of_j = find_parent(x2, y2)

            parent[parent_of_j] = parent_of_i

        def dist(pi, pj):

            return abs(pi[0] - pj[0]) + abs(pi[1] - pj[1])

        for i in range(n - 1):
            for j in range(i + 1, n):

                cost = dist(points[i], points[j])

                edges.append((cost, tuple(points[i]), tuple(points[j])))

        edges.sort(key=lambda e: e[0])

        min_cost = 0
        selected_edge = 0

        for edge in edges:

            node_v, node_u = edge[1], edge[2]
            if find_parent(*node_v) == find_parent(*node_u):
                continue

            merge(*(node_v + node_u))
            min_cost += edge[0]
            selected_edge += 1

            if selected_edge == n - 1:
                break

        return min_cost
