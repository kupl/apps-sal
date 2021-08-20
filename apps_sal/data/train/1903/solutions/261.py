class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        result = 0
        for i in range(1, len(points)):
            for j in range(i):
                edges.append((j, i, abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])))
        edges = sorted(edges, key=lambda k: k[2])
        treeId = []
        for i in range(len(points)):
            treeId.append(i)
        for (u, v, w) in edges:
            if treeId[u] != treeId[v]:
                result += w
                oldId = treeId[u]
                newId = treeId[v]
                for k in range(len(points)):
                    if treeId[k] == oldId:
                        treeId[k] = newId
        return result
