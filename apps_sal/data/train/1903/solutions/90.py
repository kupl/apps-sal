class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        costs = []
        for i in range(n):
            cost = [0] * n
            costs.append(cost)
        for i in range(n):
            ax = points[i][0]
            ay = points[i][1]
            for j in range(i + 1, n):
                bx = points[j][0]
                by = points[j][1]
                costs[i][j] = abs(ax - bx) + abs(ay - by)
                costs[j][i] = costs[i][j]
        conn = [-1] * n
        for i in range(n):
            for j in range(n):
                cs = costs[i][j]
                if cs != 0:
                    if conn[i] == -1:
                        conn[i] = j
                    elif cs < costs[i][conn[i]]:
                        conn[i] = j
        groups = []
        toset = list(range(n))
        conngroupcost = 0
        while len(toset) > 0:
            point = toset[0]
            g = [point]
            toset.remove(point)
            while conn[point] not in g:
                g.append(conn[point])
                conngroupcost += costs[point][conn[point]]
                toset.remove(conn[point])
                point = conn[point]
            while len(toset) > 0:
                npoint = []
                for x in toset:
                    if conn[x] in g:
                        npoint.append(x)
                        g.append(x)
                        conngroupcost += costs[x][conn[x]]
                if len(npoint) == 0:
                    break
                else:
                    for np in npoint:
                        toset.remove(np)
            groups.append(g)
        while len(groups) > 1:
            minlen = -1
            minindex = -1
            for gi in range(len(groups)):
                if minlen == -1:
                    minlen = len(groups[gi])
                    minindex = gi
                elif len(groups[gi]) < minlen:
                    minlen = len(groups[gi])
                    minindex = gi
            gps = groups[minindex]
            mincost = -1
            mincostp = -1
            for gp in gps:
                for i in range(n):
                    if i not in gps:
                        if mincost == -1:
                            mincost = costs[gp][i]
                            mincostp = i
                        elif mincost > costs[gp][i]:
                            mincost = costs[gp][i]
                            mincostp = i
            conngroupcost += mincost
            conngindex = -1
            for gindex in range(len(groups)):
                if mincostp in groups[gindex]:
                    conngindex = gindex
                    break
            groups[minindex] = groups[minindex] + groups[conngindex]
            del groups[conngindex]
        return conngroupcost
