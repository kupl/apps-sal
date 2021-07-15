class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        mst = [False]*n
        dist = [None]*n       
        i = 0
        dist[i] = 0
        mst[i] = True
        for _ in range(n - 1):
            min_dist = None
            next_i = None
            for j in range(n):
                if not mst[j]:
                    cur_dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    if dist[j] is None:
                        dist[j] = cur_dist
                    elif dist[j] > cur_dist:
                        dist[j] = cur_dist
                    if min_dist is None or min_dist > dist[j]:
                        min_dist = dist[j]
                        next_i = j
            i = next_i
            res += dist[i]
            mst[i] = True
        return res

