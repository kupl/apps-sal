class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        graph = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                val = abs(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
                graph.append([tuple(points[i]), tuple(points[j]), val])
        graph.sort(key=lambda x: x[-1])
        parent = {tuple(i): tuple(i) for i in points}

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            (a, b) = (find(x), find(y))
            if a != b:
                parent[a] = b
                return True
            else:
                return False
        v = 0
        n = len(points)
        res = 0
        i = 0
        while v != n - 1:
            (a, b, dist) = graph[i]
            if union(a, b):
                res += dist
                v += 1
            i += 1
        return res
