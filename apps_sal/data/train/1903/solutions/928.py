class Solution:

    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def build_graph(self, points):
        res = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                res.append([i, j, self.distance(points[i], points[j])])
        return res

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        connections = self.build_graph(points)
        connections.sort(key=lambda x: x[2])
        parents = [i for i in range(len(points))]

        def find(node):
            parent = parents[node]
            while node != parent:
                node = parent
                parent = parents[node]
            return node
        cost = 0
        for edge in connections:
            node1 = edge[0]
            node2 = edge[1]
            curr_cost = edge[2]
            if find(node1) != find(node2):
                parents[find(node2)] = find(node1)
                cost += curr_cost
        return cost
