class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ret = 0
        dis = {}
        for i in range(1, len(points)):
            dis[tuple(points[i])] = abs(points[i][0] - points[0][0]) + abs(points[i][1] - points[0][1])
        while len(dis) > 0:
            minD = min(dis.values())
            for (k, v) in dis.items():
                if v == minD:
                    toDel = k
                    break
            ret += minD
            del dis[toDel]
            for (k, v) in dis.items():
                dis[k] = min(dis[k], abs(k[0] - toDel[0]) + abs(k[1] - toDel[1]))
        return ret
