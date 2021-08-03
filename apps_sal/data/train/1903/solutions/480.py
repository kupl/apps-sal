class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dis = [math.inf for i in range(n)]
        myset = set()
        myset.add(0)
        res = 0
        pt = points[0]
        for i in range(n - 1):
            for idx, item in enumerate(points):
                if(idx in myset):
                    continue
                else:
                    dis[idx] = min(dis[idx], abs(pt[0] - item[0]) + abs(pt[1] - item[1]))
            mins = min(dis)
            res += mins
            cur = dis.index(mins)
            myset.add(cur)
            dis[cur] = math.inf
            pt = points[cur]
        return res
