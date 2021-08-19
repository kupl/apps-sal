class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        costs = []
        for i in range(len(points)):
            for k in range(i + 1, len(points)):
                (x, y) = points[i]
                (xx, yy) = points[k]
                costs.append((abs(x - xx) + abs(y - yy), i, k))
        costs.sort()
        dd = {x: x for x in range(len(points))}

        def merge(x, y, c):
            (x, y) = (find(x), find(y))
            if x != y:
                dd[x] = y
                self.ans += c
                self.groups -= 1

        def find(x):
            if dd[x] != x:
                dd[x] = find(dd[x])
            return dd[x]
        self.groups = len(points)
        self.ans = 0
        for (c, x, y) in costs:
            merge(x, y, c)
            if self.groups == 1:
                return self.ans
