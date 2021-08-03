class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0

        mapper = collections.defaultdict(dict)
        for ind1, point1 in enumerate(points):
            for ind2, point2 in enumerate(points):
                dis = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                mapper[ind1][ind2] = dis
                mapper[ind2][ind1] = dis

        cost = 0
        c = set()
        unc = set(range(n))

        min_i, min_j = None, None
        min_d = math.inf
        for i in range(n):
            for j in range(n):
                if i != j and mapper[i][j] < min_d:
                    min_i, min_j = i, j
                    min_d = mapper[i][j]
        cost += min_d
        c.add(min_i)
        c.add(min_j)
        unc.remove(min_i)
        unc.remove(min_j)

        mins = dict()
        for i in unc:
            mins[i] = min(mapper[i][min_i], mapper[i][min_j])

        while unc:
            min_i = None
            min_d = math.inf
            for i in unc:
                if mins[i] < min_d:
                    min_i = i
                    min_d = mins[i]
                # for j in c:
                    # if mapper[i][j] < min_d:
                    #     min_i = i
                    #     min_d = mapper[i][j]
            cost += min_d
            c.add(min_i)
            unc.remove(min_i)

            for i in unc:
                mins[i] = min(mins[i], mapper[i][min_i])

        return cost
