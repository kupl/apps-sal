class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find(i):
            while i != root[i]:
                root[i] = root[root[i]]
                i = root[i]
            return i

        def union(i, j):
            if rank[i] < rank[j]:
                root[i] = j
            elif rank[i] > rank[j]:
                root[j] = i
            else:
                root[j] = i
                rank[i] += 1
        n = len(points)
        graph = []
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph.append((distance, i, j))
        graph.sort()
        min_cost = 0
        root = list(range(n))
        rank = [0] * n
        for (distance, i, j) in graph:
            (root1, root2) = (find(i), find(j))
            if root1 != root2:
                union(root1, root2)
                min_cost += distance
        return min_cost
