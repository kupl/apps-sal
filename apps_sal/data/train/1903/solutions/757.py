class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        conn = [points[0]]
        if len(points) == 1:
            return 0
        points = points[1:]
        res = 0
        dists = {str(p): abs(p[0] - conn[0][0]) + abs(p[1] - conn[0][1]) for p in points}
        print(dists)
        while len(points) > 0:
            best = 100000000.0
            bestc = -1
            bestp = -1
            for (j, p) in enumerate(points):
                if dists[str(p)] < best:
                    bestp = j
                    best = dists[str(p)]
            res += best
            conn.append(points[bestp])
            np = points[bestp]
            del points[bestp]
            for p in points:
                dists[str(p)] = min(dists[str(p)], abs(p[0] - np[0]) + abs(p[1] - np[1]))
        return res
