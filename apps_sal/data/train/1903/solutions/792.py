class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parents = [i for i in range(n)]
        def dist(k, l):
            kx, ky = points[k]
            lx, ly = points[l]
            return abs(kx - lx) + abs(ky - ly)
        def getroot(node):
            while parents[node] != node:
                node = parents[node]
            return node
        lst = sorted([(dist(i, j), i, j) for i in range(n - 1) for j in range(i + 1, n)], reverse=True)
        totcost = 0
        while not all(parents[i] == parents[0] for i in range(1, n)):
            cost, i, j = lst.pop()
            ri, rj = getroot(i), getroot(j)
            if ri != rj:
                parents[i] = parents[j] = parents[ri] = parents[rj] = min(ri, rj)
                totcost += cost
            for i in range(n):
                parents[i] = getroot(i)
        return totcost
