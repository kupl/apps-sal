class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        all_edges = []
        for point1 in points:
            for point2 in points:
                if point1 != point2:
                    all_edges.append((abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]), tuple(point1), tuple(point2)))

        all_edges.sort(key=lambda x: (x[0]))

        parent = {tuple(point): tuple(point) for point in points}
        rank = {tuple(point): 1 for point in points}
        children = {tuple(point): 1 for point in points}

        def find(point1):
            if parent[point1] != point1:
                parent[point1] = find(parent[point1])
            return parent[point1]
        finish = False

        def union(point1, point2):
            parent1 = find(point1)
            parent2 = find(point2)
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += 1
                children[parent1] += children[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += 1
                children[parent2] += children[parent1]
            return
        cost = 0
        count = 0
        for edge in all_edges:
            if count == len(points) - 1:
                break
            if find(edge[1]) != find(edge[2]):
                union(edge[1], edge[2])
                cost += edge[0]
                count += 1
        return cost
