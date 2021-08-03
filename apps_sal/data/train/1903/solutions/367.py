class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        root = [i for i in range(n + 1)]

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def uni(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            root[x] = y
            return 1

        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        routes = []
        unconnected = n - 1
        costs = 0
        for i in range(n):
            for j in range(i + 1, n):
                routes.append([distance(points[i], points[j]), i, j])
        routes.sort(key=lambda l: l[0], reverse=True)
        while unconnected:
            route = routes.pop()
            if uni(route[1], route[2]):
                costs += route[0]
                unconnected -= 1
        return costs
