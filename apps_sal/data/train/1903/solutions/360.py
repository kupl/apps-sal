class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dis = []
        for i in range(len(points)):
            for j in range(i, len(points)):
                dis.append(
                    (
                        abs(points[i][0] - points[j][0])
                        + abs(points[i][1] - points[j][1]),
                        i,
                        j,
                    )
                )
        dis = sorted(dis, key=lambda x: x[0])

        joined = 1
        cost = 0
        parents = [x for x in range(len(points))]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        for edge in dis:
            if find(edge[1]) != find(edge[2]):
                joined += 1
                cost += edge[0]
                parents[find(edge[1])] = edge[2]
            if joined == len(points):
                return cost

