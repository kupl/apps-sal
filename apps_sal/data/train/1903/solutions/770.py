class Solution:
    def minCostConnectPoints(self, pt: List[List[int]]) -> int:
        if len(pt) == 1:
            return 0
        l = []
        for i in range(len(pt)):
            for j in range(len(pt)):
                l.append((i, j, abs(pt[i][0] - pt[j][0]) + abs(pt[i][1] - pt[j][1])))

        parents = list(range(len(pt)))
        wt = [0 for i in range(len(pt))]
        # print(l)

        def find(p):
            if p != parents[p]:
                parents[p] = find(parents[p])
            return parents[p]

        cost = 0
        for u, v, dist in sorted(l, key=lambda x: x[2]):  # sorted(l, key = lamda x:x[2]):
            pu, pv = find(u), find(v)
            if pu == pv:
                continue
            print((pu, pv, dist))
            cost += dist
            if wt[pu] >= wt[pv]:
                parents[pu] = pv
                wt[pu] += 1
            else:
                parents[pv] = pu
                wt[pv] += 1
        return cost
