class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dist = [math.inf] * N
        prev_node = 0
        res = 0

        def getDistance(x, y):
            return abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        for _ in range(N):
            (min_dist, min_dist_node) = (math.inf, -1)
            for i in range(N):
                if dist[i] != None:
                    dist[i] = min(dist[i], getDistance(prev_node, i))
                    if dist[i] < min_dist:
                        (min_dist, min_dist_node) = (dist[i], i)
            res += min_dist
            prev_node = min_dist_node
            dist[prev_node] = None
        return res
