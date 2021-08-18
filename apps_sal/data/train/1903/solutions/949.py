class Solution:
    def minCostConnectPoints(self, points) -> int:
        p_set = [i for i in range(len(points))]

        def father(i):
            while p_set[i] != i:
                i = p_set[i]
            return i
        if len(points) == 1:
            return 0

        edge = {}
        edgelist = []
        res = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                le = 0
                le += abs(points[i][1] - points[j][1])
                le += abs(points[i][0] - points[j][0])
                if le in edge:
                    edge[le].append((i, j))
                else:
                    edge[le] = [(i, j)]
                    edgelist.append(le)
        edgelist.sort()
        (i, j) = edge[edgelist[0]][0]
        res += edgelist[0]
        p_set[j] = i
        for key in edgelist:
            for (i, j) in edge[key]:
                fi = father(i)
                fj = father(j)
                if fj != fi:
                    p_set[fj] = fi
                    res += key
        return res
