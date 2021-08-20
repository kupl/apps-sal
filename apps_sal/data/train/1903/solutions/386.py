class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, distance))
        edges.sort(key=itemgetter(2))
        numComponents = len(points)
        groups = [i for i in range(len(points))]
        size = [1] * len(points)

        def find(x):
            if groups[x] == x:
                return x
            groups[x] = find(groups[x])
            return groups[x]
        cost = 0
        for edge in edges:
            p1 = edge[0]
            p2 = edge[1]
            root1 = find(p1)
            root2 = find(p2)
            if root1 != root2:
                if size[p1] < size[p2]:
                    groups[root1] = groups[root2]
                    size[root2] += size[root1]
                else:
                    groups[root2] = groups[root1]
                    size[root1] += size[root2]
                cost += edge[2]
                numComponents -= 1
        if numComponents == 1:
            return cost
        else:
            return -1
