class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        cc = [i for i in range(len(points))]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        edges.sort()

        def root(x):
            if cc[x] != x:
                cc[x] = root(cc[x])
            return cc[x]

        def join(x, y):
            rx = root(x)
            ry = root(y)
            if rx != ry:
                cc[rx] = ry
            return rx != ry

        cct = len(points)
        cost = 0
        # print('foo')
        for x, i, j in edges:
            if join(i, j):
                cost += x
                # print(x)
                cct -= 1
                if cct == 1:
                    break
        return cost
