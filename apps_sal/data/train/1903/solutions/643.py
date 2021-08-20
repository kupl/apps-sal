class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        diss = [[0] * n for _ in range(len(points))]
        res = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                length = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                diss[i][j] = diss[j][i] = length
        disinfo = []
        for info in diss:
            tmp = []
            for (i, l) in enumerate(info):
                tmp.append((l, i))
            tmp.sort(reverse=True)
            disinfo.append(tmp)
        not_linked = set(range(1, len(points)))
        min_dis = diss[0].copy()
        min_dis[0] = math.inf
        while not_linked:
            nxt_dis = min(min_dis)
            res += nxt_dis
            nxt = min_dis.index(nxt_dis)
            not_linked.remove(nxt)
            min_dis[nxt] = math.inf
            for i in range(len(points)):
                if min_dis[i] < math.inf:
                    min_dis[i] = min(diss[nxt][i], min_dis[i])
        return res
