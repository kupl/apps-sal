class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = {tuple(points[0]): 0}
        p = points[0]
        res = 0
        while p:
            min_dist = float('inf')
            np = None
            for point in points:
                if tuple(point) not in dist or dist[tuple(point)] > 0:
                    new_d = abs(point[0] - p[0]) + abs(point[1] - p[1])
                    dist[tuple(point)] = min(new_d, dist[tuple(point)]) if tuple(point) in dist else new_d
                if dist[tuple(point)] > 0 and dist[tuple(point)] < min_dist:
                    min_dist = dist[tuple(point)]
                    np = point
            p = np
            if p:
                res += min_dist
                dist[tuple(p)] = 0
        return res
